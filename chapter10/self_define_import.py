import sys
import importlib.abc
import imp
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from html.parser import HTMLParser

# Debugging
import logging
log = logging.getLogger(__name__)

# Get links from a given URL
def _get_links(url):
    class LinkParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == 'a':
                attrs = dict(attrs)
                links.add(attrs.get('href').rstrip('/'))
    links = set()
    try:
        log.debug(f'Getting links from {url}')
        u = urlopen(url)
        parser = LinkParser()
        parser.feed(u.read().decode('utf-8'))
    except Exception as e:
        log.debug(f'Could not get links. {e}')
    log.debug(f'links: {links}')
    return links

class UrlMetaFinder(importlib.abc.MetaPathFinder):
    def __init__(self, base_url):
        self._base_url = base_url
        self._links = {}
        self._loaders = {base_url : UrlModuleLoader(base_url)}

    def find_module(self, full_name, path=None):
        log.debug(f'find_module: full_name={full_name}, path={path}')
        if path is None:
            base_url = self._base_url
        else:
            if not path[0].startswith(self._base_url):
                return None
            base_url = path[0]
        parts = full_name.split('.')
        base_name = parts[-1]
        log.debug(f'find_module: base_url={base_url}, base_name={base_name}')

        # Check link cache
        if base_name not in self._links:
            self._links[base_url] = _get_links(base_url)

        # Check if it's a package
        if base_name in self._links[base_url]:
            log.debug(f'find_module: trying package {full_name}')
            full_url = self._base_url + '/' + base_name
            # Attempt to load the package (which accesses __init__.py)
            loader = UrlPackageLoader(full_url)
            try:
                loader.load_module(full_name)
                self._links[full_url] = _get_links(full_url)
                self._loaders[full_url] = UrlModuleLoader(full_url)
                log.debug(f'find_module: package {full_name} loaded')
            except ImportError as e:
                log.debug(f'find_module: package failed. {e}')
                loader = None
            return loader
        # A normal module
        file_name = base_name + '.py'
        if file_name in self._links[base_url]:
            log.debug(f'find_module: module {full_name} found')
            return self._loaders[base_url]
        else:
            log.debug(f'find_module: module {full_name} not found')
            return None

    def invalidate_caches(self):
        log.debug('invalidating link cache')
        self._links.clear()

# Module Loader for a URL
class UrlModuleLoader(importlib.abc.SourceLoader):
    def __init__(self, base_url):
        self._base_url = base_url
        self._source_cache = {}

    def module_repr(self, module):
        return f'<urlmodule {module.__name__} from {module.__file__}>'

    # Required method
    def load_module(self, full_name):
        code = self.get_code(full_name)
        mod = sys.modules.setdefault(full_name, imp.new_module(full_name))
        mod.__file__ = self.get_filename(full_name)
        mod.__loader__ = self
        mod.__package__ = full_name.rpartition('.')[0]
        exec(code, mod.__dict__)
        return mod

    # Optional extensions
    def get_code(self, full_name):
        src = self.get_source(full_name)
        return compile(src, self.get_filename(full_name), 'exec')

    def get_data(self, path):
        pass

    def get_filename(self, full_name):
        return self._base_url + '/' + full_name.split('.')[-1] + '.py'

    def get_source(self, full_name):
        file_name = self.get_filename(full_name)
        log.debug(f'loader: reading {file_name}')
        if file_name in self._source_cache:
            log.debug(f'loader: cached {file_name}')
            return self._source_cache[file_name]
        try:
            u = urlopen(file_name)
            source = u.read().decode('utf-8')
            log.debug(f'loader: {file_name} loaded')
            self._source_cache[file_name] = source
            return source
        except (HTTPError, URLError) as e:
            log.debug(f'loader: {file_name} failed. {e}')
            raise ImportError(f"Can't load {file_name}")

    def is_package(self, full_name):
        return False

# Package loader for a URL
class UrlPackageLoader(UrlModuleLoader):
    def load_module(self, full_name):
        mod = super().load_module(full_name)
        mod.__path__ = [ self._base_url ]
        mod.__package__ = full_name

    def get_filename(self, full_name):
        return self._base_url + '/' + '__init__.py'

    def is_package(self, full_name):
        return True

# Utility functions for installing/uninstalling the loader
_installed_meta_cache = {}
def install_meta(address):
    if address not in _installed_meta_cache:
        finder = UrlMetaFinder(address)
        _installed_meta_cache[address] = finder
        sys.meta_path.append(finder)
        log.debug(f'{finder} installed on sys.meta_path')

def remove_meta(address):
    if address in _installed_meta_cache:
        finder = _installed_meta_cache.pop(address)
        sys.meta_path.remove(finder)
        log.debug(f'{finder} removed from sys.meta_path')
