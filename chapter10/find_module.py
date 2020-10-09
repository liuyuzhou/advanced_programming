class Finder(object):
    def find_module(self, full_name, path):
        print(f'Looking for {full_name} {path}')
        return None


import sys
sys.meta_path.insert(0, Finder())
import math
print('finish import math\n')

import types
print('finish import types\n')

print('import threading')
import threading


print('\n')
import xml.etree.ElementTree


del sys.meta_path[0]
sys.meta_path.append(Finder())
import requests
import time
