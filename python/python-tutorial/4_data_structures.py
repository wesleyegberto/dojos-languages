# Data Structures

# By convension, the mutable methods return always None.

# === List ===
list = [1, 2]

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

## Comprehensions
# long way
squares = []
for x in range(10):
    squares.append(x ** 2)

squares = list(map(lambda x: x ** 2, range(10)))

# short form
squares = [x ** 2 for x in range(10)]


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

matrix_T = list(zip(*matrix))


# === List as Stack (LIFO) ===
# Just use append and pop (this operations are fast)
stack = []
stack.append(1)
stack.append(2)
stack.pop() # 2
stack.pop() # 1


# === Deque as Queue (FIFO) ===
# Add or rem elements to the beginning of the list is slow because the others have to shift one place.
# Better use `Deque`

from collection import deque
queue = deque([0, 1, 2])
queue.append(3)
queue.append(4)
queue.popleft() # 0
queue.popleft() # 1


# === Tuples ===
# consist of values separated by comma and are immutable
origin = 0, 0, 0 # we can ommit the parentheses sometimes (when the expression is not so complex)

empty = ()
singleton = 'one', # ('one',): we must provide comma at the end 

# origin[0] = 1 # error

x = origin[0] # we can access using []
y, z = origin[1:3] # and using range :

x, y, z = origin # unpacking every element

nested_tuple = (origin, (1, 1, 1)) # can contain any type


# === Set ===
# unordered collection with no duplicate elements
empty_set = set() # empty set (we can't use {})
set_1 = { 'John', 'Joana' } # create a set with two name
set_2 = set(['John', 'Joana']) # create the same set but using set

unique_letters = set('Joana') # unique letters from the string

'John' in set_1 # True

# we can operate over them
a = set('john')
b = set('joana')

a - b # letters in a but not in b
a | b # OR: letters in a or b
a & b # AND: letters in a and b
a ^ b # XOR: letters in a or b but not both

# comprehension
{x for x in 'abracadabra' if x not in 'abc'}


# === Dictionaries ===
# collection of key-value where the key could be any immutable type
empty = {}
ages = {'john': 42, 'joana': 24}

ages = dict([('john', 42), ('joana', 24)])

ages['john'] # 42
ages['john'] = 43

ages['lucio'] = 15

del ages['lucio']

list(ages) # list of keys

sorted(ages) # list of sorted keys

'john' in ages # True


# === Looping techniques ===

# we can use items() to loop through key-value
for name, age in ages.items():
    print(name, ':', age)

# loop a sequence getting the index
for index, hero in enumerate(['hulk', 'wolverine', 'professor x']):
    print(index, hero)

# loop over two sequences
countries = ['Brazil', 'France', 'USA']
cities = ['Sao Paulo', 'Paris', 'New York']
for country, city in zip(countries, cities):
    print('{1} is in {0}'.format(country, city))

# loop over a sequence in reverse
for i in reversed(range(1, 10, 2)):
    print(i)

