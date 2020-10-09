def func(n):
    return n + 10

func('Hello')


import pdb
pdb.pm()


import traceback
import sys

try:
    func(arg)
except:
    print('**** AN ERROR OCCURRED ****')
    traceback.print_exc(file=sys.stderr)


def sample(n):
    if n > 0:
        sample(n-1)
    else:
        traceback.print_stack(file=sys.stderr)

sample(5)


import pdb

def func(arg):
    ...
    pdb.set_trace()
    ...