# Author: OMKAR PATHAK
# In this example we will see how to write list comprehensions to make our tasks easier

# Python.org says:
# List comprehensions provide a concise way to create lists.
# Common applications are to make new lists where each element is
# the result of some operations applied to each member of another sequence
# or iterable, or to create a subsequence of those elements that satisfy a certain condition.

numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)              # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Side Effect of above operation:It creates a variable(or overwrites) named 'x'
# that still exists after the loop completes. To get rid of this Side Effect we use List comprehensions.

# List comprehension:
numbers = [i for i in range(10)]
print(numbers)              # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Let us see few more examples
squares = [i * i for i in range(10)]
print(squares)            
squares = []
for i in range(10):
    squares.append(i * i)

# Some more:
odds = [i for i in numbers if i % 2 != 0]
print(odds)                 # [1, 3, 5, 7, 9]

# This is same as:
odds = []
for i in numbers:
    if i % 2 != 0:
        odds.append(i)

def isSqaure(x):
    import math
    sqrt = int(math.sqrt(x))
    return x == sqrt * sqrt

squares = [x for x in range(100) if isSqaure(x) == True]
print(squares)            
pairs = [[x, x * x] for x in numbers]
print(pairs)              
