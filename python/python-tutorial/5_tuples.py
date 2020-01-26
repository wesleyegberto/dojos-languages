# Tuples

# consist of values separated by comma and are immutable
origin = 0, 0, 0 # we can ommit the parentheses sometimes (when the expression is not so complex)

empty = ()
tuple_of_letters = tuple('hello') # tuple of letters from the word

single = tuple(['one'])
single = ('one',)
single = 'one', # ('one',): we must provide comma at the end

# origin[0] = 1 # error

x = origin[0] # we can access using []
y, z = origin[1:3] # and using range :

x, y, z = origin # unpacking every element

nested_tuple = (origin, (1, 1, 1)) # can contain any type
