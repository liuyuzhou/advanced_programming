import importlib
import sys
from collections import defaultdict

_post_import_hooks = defaultdict(list)

class PostImportFinder:
    def __init__(self):
        self._skip = set()

    def find_module(self, full_name, path=None):
        if full_name in self._skip:
            return None
        self._skip.add(full_name)
        return PostImportLoader(self)

class PostImportLoader:
    def __init__(self, finder):
        self._finder = finder

    def load_module(self, full_name):
        importlib.import_module(full_name)
        module = sys.modules[full_name]
        for func in _post_import_hooks[full_name]:
            func(module)
        self._finder._skip.remove(full_name)
        return module

def imported_action(full_name):
    def decorate(func):
        if full_name in sys.modules:
            func(sys.modules[full_name])
        else:
            _post_import_hooks[full_name].append(func)
        return func
    return decorate

sys.meta_path.insert(0, PostImportFinder())