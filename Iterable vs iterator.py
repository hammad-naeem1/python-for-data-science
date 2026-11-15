# 1. This list is an ITERABLE (you can loop over it, but it has no __next__ method)
my_list = [10, 20, 30]

# 2. Get an ITERATOR from the iterable using iter()
my_iterator = iter(my_list)

# 3. Use next() on the iterator to fetch items one by one
print(next(my_iterator))  # Output: 10
print(next(my_iterator))  # Output: 20
print(next(my_iterator))  # Output: 30

# 4. Calling next() again raises StopIteration because the iterator is exhausted
try:
  print(next(my_iterator))
except StopIteration:
  print("Iterator is exhausted!")
