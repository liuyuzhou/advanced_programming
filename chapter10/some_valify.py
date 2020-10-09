# from pprint import pprint
# import sys
#
# print('sys.path is:')
# pprint(sys.path)
#
#
# print('sys.path_importer_cache is:')
# pprint(sys.path_importer_cache)


class Finder(object):
    def find_loader(self, name):
        print(f'Looking for {name}')
        return None, []
#
import sys
# sys.path_importer_cache['debug'] = Finder()
# sys.path.insert(0, 'debug')
# import threading


# sys.path_importer_cache.clear()
#
# def check_path(path):
#     print(f'Checking {path}')
#     raise ImportError()
#
# sys.path_hooks.insert(0, check_path)
# import fib
#
#
# def check_url(path):
#     if path.startswith('http://'):
#         return Finder()
#     else:
#         raise ImportError()
#
# sys.path.append('http://localhost:15000')
# sys.path_hooks[0] = check_url
# # import fib
# sys.path_importer_cache['http://localhost:15000']
#
#
import xml.etree.ElementTree
xml.__path__
xml.etree.__path__
#
#
# # if self._links is None:
# #     self._links = [] # See discussion
# #     self._links = _get_links(self._baseurl)
#
#
# import logging
# logging.basicConfig(level=logging.DEBUG)
# from chapter10 import self_define_import_1
# self_define_import_1.install_path_hook()
# # import fib
# import sys
# sys.path.append('http://localhost:15000')
# import fib