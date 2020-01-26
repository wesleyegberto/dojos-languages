# Arrays
# Like a list but only store elements of same type

# we need to import
from array import *

# To create a array we can pass a parameter to define the byte size of the elements

# Param | Details
#  b    |  Represents signed integer of size 1 byte
#  B    |  Represents unsigned integer of size 1 byte
#  c    |  Represents character of size 1 byte
#  u    |  Represents unicode character of size 2 bytes
#  h    |  Represents signed integer of size 2 bytes
#  H    |  Represents unsigned integer of size 2 bytes
#  i    |  Represents signed integer of size 2 bytes
#  I    |  Represents unsigned integer of size 2 bytes
#  w    |  Represents unicode character of size 4 bytes
#  l    |  Represents signed integer of size 4 bytes
#  L    |  Represents unsigned integer of size 4 bytes
#  f    |  Represents floating point of size 4 bytes
#  d    |  Represents floating point of size 8 bytes

my_array = array('i', [1, 2, 3])
other_array = array('i', [5, 6])

my_array[0]
my_array.count(1) # count the occurrences of 1


# === Operations ===
# have methods like list

my_array.append(4) # [1, 2 , 3, 4]
my_array.insert(0, -1) # [-1, 1, 2, 3, 4]

my_array.extend(other_array) # [-1, 1, 2, 3, 4, 5, 6]

my_array.fromlist([7, 8]) # [-1, 1, 2, 3, 4, 5, 6, 7, 8]

my_array.remove(-1) # remove value

my_array.pop() # remove last

# accessing by one-based index
my_array.index(1) # first element