# Set

# unordered collection with no duplicate elements, the elements must be hashable (implements `__hash__()` and `__eq__()`)
empty_set = set() # empty set (we can't use {})
set_1 = { 'John', 'Joana' } # create a set with two name
set_2 = set(['John', 'Joana']) # create the same set but using set

unique_letters = set('Joana') # set of letters from the string

'John' in set_1 # True

# comprehension
{x for x in 'abracadabra' if x not in 'abc'}


# we can have set of set (because it ins't hashable)
{{1, 2}, {3, 4}} # TypeError: unhashable type: 'set'

# We can use frozenset
{frozenset({1, 2}), frozenset({3, 4})}


# === Operations ===

# Between elements
2 in {1,2,3} # True
4 in {1,2,3} # False
4 not in {1,2,3} # True

# Add and Remove
s = {1,2,3}
s.add(4) # s == {1,2,3,4}

s.discard(3) # s == {1,2,4} 
s.discard(5) # s == {1,2,4} 

s.remove(2) # s == {1,4}
s.remove(2) # KeyError!

# Between sets (immutable operations)
a = set('john')
b = set('joana')
a - b # letters in a but not in b
a | b # OR: letters in a or b
a & b # AND: letters in a and b
a ^ b # XOR: letters in a or b but not both

# Intersection
{1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}) # {3, 4, 5}
{1, 2, 3, 4, 5} & {3, 4, 5, 6} # {3, 4, 5}

# Union
{1, 2, 3, 4, 5}.union({3, 4, 5, 6}) # {1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5} | {3, 4, 5, 6} # {1, 2, 3, 4, 5, 6}

# Difference
{1, 2, 3, 4}.difference({2, 3, 5}) # {1, 4}
{1, 2, 3, 4} - {2, 3, 5} # {1, 4}

# Symmetric difference with (XOR)
{1, 2, 3, 4}.symmetric_difference({2, 3, 5}) # {1, 4, 5}
{1, 2, 3, 4} ^ {2, 3, 5} # {1, 4, 5}

# Superset check
{1, 2}.issuperset({1, 2, 3}) # False
{1, 2} >= {1, 2, 3} # False

# Subset check
{1, 2}.issubset({1, 2, 3}) # True
{1, 2} <= {1, 2, 3} # True

# Disjoint check
{1, 2}.isdisjoint({3, 4}) # True
{1, 2}.isdisjoint({1, 4}) # False

# Between sets (mutable operations)
# method        | in-place operation | in-place method
# union         |  s |= t            |  update
# intersection  |  s &= t            |  intersection_update
# difference    |  s -= t            |  difference_update

s = {1, 2}
s.update({3, 4}) # s == {1, 2, 3, 4}
