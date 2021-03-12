"""
filter, map, reduce
"""
from functools import reduce


def add_all(a, b):
    return a+b


nums = [3, 2, 6, 8, 4, 6, 2, 9]
evens = list(filter(lambda n: n % 2 == 0, nums))

doubles = list(map(lambda n: n*2, evens))
total = reduce(add_all, doubles)


print(evens)
print(doubles)
print(total)