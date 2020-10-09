import pickle

data_obj = ... # Some Python object
test_file = open('test_file', 'wb')
pickle.dump(data_obj, test_file)


p_con = pickle.dumps(data_obj)


# Restore from a file
test_file = open('test_file', 'rb')
data_obj = pickle.load(test_file)

# Restore from a string
data_obj = pickle.loads(p_con)


import pickle
test_file = open('some_data', 'wb')
pickle.dump([1, 6, 3, 9], test_file)
pickle.dump('hello,world!', test_file)
pickle.dump({'python', 'java', 'go'}, test_file)
test_file.close()
test_file = open('some_data', 'rb')
print(f'file load is {pickle.load(test_file)}')
print(f'file load is {pickle.load(test_file)}')
print(f'file load is {pickle.load(test_file)}')


import math
import pickle
print(f'pickle funciton: {pickle.dumps(math.cos)}')


import time
import threading

class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print(f'T-minus is: {self.n}')
            self.n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)


count_down = Countdown(30)

test_file = open('test.p', 'wb')
import pickle
pickle.dump(count_down, test_file)
test_file.close()


test_file = open('test.p', 'rb')
print(f'load result: {pickle.load(test_file)}')