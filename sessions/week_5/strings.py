import numpy

string_format = "{0:4} {2:6} {3:8} {1:7.4f}"

for i in numpy.arange(0, 11, 0.5):
    print(string_format.format(i, i ** .5, i ** 2, i ** 3))
