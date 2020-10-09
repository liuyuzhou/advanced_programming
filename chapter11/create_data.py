import numpy
from socket import *
from chapter11.big_data import send_from, recv_into

a = numpy.arange(0.0, 50000000.0)
c = socket(AF_INET, SOCK_STREAM)
send_from(a, c)

# Client
import numpy
a = numpy.zeros(shape=50000000, dtype=float)
print(a[0:10])
recv_into(a, c)
c = socket(AF_INET, SOCK_STREAM)
print(a[0:10])