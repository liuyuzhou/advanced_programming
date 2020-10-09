import sys
import csv

with open(sys.argv[1]) as f:
     for row in csv.reader(f):

         # Some kind of processing
         pass


import sys
import csv

def main(filename):
    with open(filename) as f:
         for row in csv.reader(f):
             # Some kind of processing
             pass

main(sys.argv[1])


import math
import time

def compute_roots(nums):
    result = []
    for n in nums:
        result.append(math.sqrt(n))
    return result

begin_time = time.time()
nums = range(1000000)
for n in range(100):
    r = compute_roots(nums)
print(f'time spend: {time.time() - begin_time}s')

from math import sqrt

def compute_roots(nums):

    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result

begin_time = time.time()
nums = range(1000000)
for n in range(100):
    r = compute_roots(nums)
print(f'time spend: {time.time() - begin_time}s')



import math

def compute_roots(nums):
    sqrt = math.sqrt
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result


class SomeClass:
    ...
    def method(self):
         for x in s:
             op(self.value)

# Faster
class SomeClass:

    ...
    def method(self):
         value = self.value
         for x in s:
             op(value)


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value


from timeit import timeit
a = A(1,2)
print(f"a.x time spend: {timeit('a.x', 'from __main__ import a')}s")
print(f"a.y time spend: {timeit('a.y', 'from __main__ import a')}s")