import warnings

def func(x, y, log_file=None, debug=False):
    if log_file is not None:
         warnings.warn('log_file argument deprecated', DeprecationWarning)
    ...

func(1, 2, 'a')

import warnings
warnings.simplefilter('always')
f = open('/etc/passwd')
del f