def ds(x):
    return 2 * x + 1


print(ds(5))
# lambda表达式
g = lambda x: 2 * x + 1
print(g(5))

add = lambda x, y: x + y
print(add(3, 4))
# BIF
print('filter()'.center(20))
help(filter)
# Help on class filter in module builtins:
#
# class filter(object)
#  |  filter(function or None, iterable) --> filter object
#  |
#  |  Return an iterator yielding those items of iterable for which function(item)
#  |  is true. If function is None, return the items that are true.
#  |
#  |  Methods defined here:
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |
#  |  __next__(self, /)
#  |      Implement next(self).
#  |
#  |  __reduce__(...)
#  |      Return state information for pickling.
print(filter(None, [1, 0, False, True]))
print(list(filter(None, [1, 0, False, True])))


def odd(x):
    return x % 2


print(type(odd))
temp = range(10)
show = filter(odd, temp)
print(list(show))

odd = lambda x: x % 2
print(list(filter(odd, range(10))))

print(list(filter(lambda x: x % 2, range(10))))
print("map()".center(20))
print(help(map))
# class map(object)
#  |  map(func, *iterables) --> map object
#  |
#  |  Make an iterator that computes the function using arguments from
#  |  each of the iterables.  Stops when the shortest iterable is exhausted.
#  |
#  |  Methods defined here:
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |
#  |  __next__(self, /)
#  |      Implement next(self).
#  |
#  |  __reduce__(...)
#  |      Return state information for picklin

print(list(map(lambda x: x * 2, range(10))))
