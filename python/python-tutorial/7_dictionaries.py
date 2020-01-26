# Dictionaries

# collection of key-value where the key could be any immutable type
empty = {}
empty = dict()
empty = dict([])

one_key = dict(key='value')
one_key = dict([('key', 'value')])

ages = {'john': 42, 'joana': 24}

ages = dict([('john', 42), ('joana', 24)])

ages['john'] # 42
ages['john'] = 43

ages['lucio'] = 15

del ages['lucio']

list(ages) # list of keys

sorted(ages) # list of sorted keys

'john' in ages # True


# Shallow copy
all_ages = { **ages }


# === Looping ===

for key in ages.keys():
    print('{} is {} years old'.format(key, ages[key]))

# we can use items() to loop through key-value
for name, age in ages.items():
    print(name, ':', age)

for key in ages.keys():
    print(key, ages[key])

for value in ages.values():
    print(value)


# === Default values for keys ===

from collections import defaultdict
empty_dict = defaultdict(int)

empty_dict['key'] # 0
empty_dict['key'] = 10
empty_dict['key'] # 10


# === Merge dicts ===
from collections import ChainMap
merged = dict(ChainMap(map1, map2))


# === Comprehensions ===

# creating a new
squares = {x: x ** 2 for x in [1, 2, 3, 4]} # {1: 1, 2: 4, 3: 9, 4: 16}

dict((x, x * x) for x in (1, 2, 3, 4))

