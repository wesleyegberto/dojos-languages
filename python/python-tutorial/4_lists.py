 Data Structures

# By convension, the mutable methods return always None.

# === List ===
# mutable collection of values of any type
# insertion order
empty_list = list()
also_empty = []

# checking if is empty
len(empty_list) == 0
not empty_list

list = [1, 2]
letters = list('world') # list of letters

# accessing its elements
numbers = [1, 2, 3, 4]
numbers[0] # 1
numbers[-1] # 4

# slicing returns a new list
numbers[0:2] # [1, 2]
numbers[:2] # [1, 2]

numbers[2:4] # [3, 4]
numbers[2:] # [3, 4]

numbers[-1] # 4
numbers[-3:-1] # [3, 4]

numbers[-3:] # [2, 3, 4]

# shallow copy (keeping same reference)
copy = numbers[:]

# lists are mutable
numbers = [1, 2, 3, 4]
numbers[0] = 10 # [0, 2, 3, 4]
numbers = numbers + 10

# more efficient way to append at the end
numbers.append(11)
numbers.append(12)

# slicing changing
numbers[0:2] = [1, 2]
numbers[5:] = [] # removing elements from index 4
numbers[:] = [] # clear the list

# list concat
long_numbers = numbers + [5, 6, 7, 8, 9]

# list methods
list.append(3) # insert at the end
list.extend([4, 5]) # insert all at the end

list.insert(0, 0) # insert 2 at index 0
list.insert(len(list), 6) # append

list.pop() # remove and return last elem (6)

del list[5] # remove the elem at index 5
del list[3:5] # remove the elems at index 3 and 4

list.remove(0) # remove elem 0

list.reverse()

list.copy() # like list[:]

# iterating
lst = [1, 2, 3, 4]

for value in lst:
	print(lst)

for index, value in enumerate(lst):
	print('{} is at position {}'.format(value, index))

## Comprehensions
# long way
squares = []
for x in range(10):
    squares.append(x ** 2)

squares = list(map(lambda x: x ** 2, range(10)))

# short form
squares = [x ** 2 for x in range(10)]

# filter

saquares_greater_10 = [x ** 2 for x in range(100) if x ** 2 > 10] # slow - calculates twice
saquares_greater_10 = [v for v in (x ** 2 for x in range(100)) if v > 10] # fast



# long version
first_pows = []
for x in [1, 2, 3]:
    for y in [1, 2, 3]:
        first_pows.append(x ** y)

# short version
first_pows = [x ** y for x in [1, 2, 3] for y in [1, 2, 3]]


odds_squares = [x ** 2 for x in range(10) if x % 2 == 1]

# Nesting
matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

matrix_T = [[row[i] for row in matrix] for i in range(3)]

# unpacking the rows
matrix_T = list(zip(*matrix))


values = [1, 1, 0]

# return True if all evals True
all(values) # False
all(val > 0 for val in values)

# return True if any evals True
any(values) # True
any(val > 0 for val in values)


