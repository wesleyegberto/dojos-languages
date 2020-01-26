# Basic Types and Operations
# - bool
# - int
# - complex
# - float
# - string
# - list
# - set
# - tuple
# - map

# === bool ===

is_true = True
is_false = False

# bool is subtype of int
issubclass(bool, int) # true
isinstance(True, int) # true
isinstance(False, int) # true

True + False # 1 + 0 = 1
True * True # 1 * 1 = 1
False - False # 0 - 0 = 0

# === int ===
# integer numbers have type `int`
x = 1
y = 2
z = 0
k = 9223372036854775807
type(k) # <type 'int'>

k = int('123') # converting
k = int('1.3') # ValueError

# === float ===
# fractional part have type `float`
w = 102.3
s = 15.35
pi = 3.14
type(pi) # <type 'float'>

pi = float('3.14')

# === complex ===
# complex numbers (sufix `j` or `J`)
j = (2 + 3j)
i = (1 + 5j)
r = j + (3 + 10j)
type(r) # <type 'complex'>

# === None ===
# type to indicate the absence of value
x = None
type(x) # <type 'NoneType'>


# === Basic Operations ===

# in Python 3, division always returns a float (in Python 2, returns an int)
17 / 3 # 5.666666666666667
15 / 3 # 5.0

# floor division: discard fractional part and returns a int
17 // 3 # 5

# remainder operation (%)
17 % 3 # 2

# power operation (**)
5 ** 2 # 25
2 ** 7 # 128


# Math

import math # simple numbers
import cmath # complex numbers

c = 4
math.sqrt(c) # = 2.0 (always float; does not allow complex results)
cmath.sqrt(c) # = (2+0j) (always complex)

math.exp(0) # 1.0
math.exp(1) # 2.718281828459045 (e)

# better precision: `expm1` is (e ** x) - 1
math.expm1(0) # 0.0
math.exp(1e-6) - 1 # 1.0000004999621837e-06
math.expm1(1e-6) # 1.0000005000001665e-06

a, b = 1, 2
math.sin(a)
math.cosh(b)
math.atan(math.pi)
math.hypot(a, b)

math.degrees(a)
math.radians(57.29577951308232)

math.log(5) # 1.6094379124341003
cmath.log(5) # (1.6094379124341003 + 0j)

# second arg is the base
math.log(5, math.e) # 1.6094379124341003
math.log(1000, 10) # 3.0 (always returns float)
cmath.log(1000, 10) # (3 + 0j)

# Logarithm base e - 1 (higher precision for low values)
math.log1p(5) # 1.791759469228055

# Logarithm base 2
math.log2(8) # 3.0

# Logarithm base 10
math.log10(100) # 2.0
cmath.log10(100) # (2 + 0j)


# === Strings ===
# can be single or double quotes
name = 'John Doe'
power = "fly"
nickname = 'John\'s Lost'
type(name) # <type 'string'>

# we can use `r` to not escape the \
raw_string = r'C:\Users\nonsense'

# `f` to interpolation
x = 42
answer = f'Universe answer: {x:3d}' # prints it with a string of size 3 (padding with spaces)

# format()
answer = '{:-20} answer: {:2.2}'.format('Universe', x)

answer = '{text:-20} answer: {answer:2.2}'.format(text='Universe', answer=x) # format with var names
answer = '{1:-20} answer: {0:2.2}'.format(x, 'Universe') # format with positions

# format with dict
calculation = {text: 'Universe', answer: 42}
answer = '{0[text]:-20} answer: {0[answer]:2.2}'.format(calculation) # accessing by key
answer = '{text:-20} answer: {answer:2.2}'.format(**calculation) # unpacking


# we can use: !a for ascii(), !s for str() and !r for repr()
answer = f'Universe answer: {42!s}'

# multiline string
print("""
Multiline string
    will keep the format
""")

# === String Operations ===
# concat
"Hello" + " " + "World"

# two or more string literals will be concatened
"Hello" " " "World"
text = ("Here is a line easy to read "
       " and here is its continuation.")

# Repeat
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

# Converting
str_age = str(42) # convert to a human-readable format
str_size = repr(42) # convert to a machine-readable format - format that can be evaluated later with `eval()`
