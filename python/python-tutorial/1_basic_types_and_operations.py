# Basic Types and Operations
# - int
# - float
# - string
# - list
# - map

# === Numerical Types ===

# Basic Types 

# integer numbers have type `int`
x = 2
y = 3
z = 100

# fractional part have type `float`
weight = 102.3
size = 15.35

# complex numbers (sufix `j` or `J`)
(2 + 3J) + (1 + 3j)


# Basic Operations

# in Python 3, division always returns a float (in Python 2, returns an int)
17 / 3 # 5.666666666666667
15 / 3 # 5.0

# floor division (discard fractional part) returns a int
17 // 3 # 5

# remainder operation (%)
17 % 3 # 2

# power operation (**)
5 ** 2 # 25
2 ** 7 # 128

 
# === Strings ===
# can be single or double quotes
name = 'John Doe'
power = "fly"
nickname = 'John\'s Lost'

# we can use `r` to not escape the \n
raw_string = r'C:\Users\nonsense'

# multiline string
print("""
Multiline string
    will keep the format
""")

# String Operations
# concat
"Hello" + " " + "World"

# two or more string letals will be concatened
"Hello" " " "World"
text = ("Here is a line easy to read "
       " and here is its continuation.")

# repeat
"Hi" * 3

word = "Java"

word[0] # J
word[1] # a

word[-1] # a
word[-2] # v

# slicing string
word[0:2] # Ja
word[:2] # Ja
word[2:4] # va
word[2:] # va
word[-2:] # va
word[:-2] # Ja

len(word) # 4


# === Lists ===
numbers = [1, 2, 3, 4]
numbers[0] # 1
numbers[-1] # 4

# slicing returns a new list
numbers[-3:] # [2, 3, 4]
# shallow copy (keeping same reference)
copy = numbers[:]
 
# list concat
long_numbers = numbers + [5, 6, 7, 8, 9]

# lists are mutable
numbers[0] = 10
numbers = numbers + 10

# more efficient
numbers.append(11)
numbers.append(12)

# slicing changing
numbers[0:2] = [1, 2]
numbers[5:] = [] # removing elements from index 4
numbers[:] = [] # clear the list
