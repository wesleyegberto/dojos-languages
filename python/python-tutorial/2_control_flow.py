#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Control Flow

# === if ===
x = 10

if x < 0:
    print('Negative number')
elif x == 0:
    print('Zero')
else:
    print('Positive number')

# ternary
val = 10 if x > 10 else 20

# nested ternary
val = False if x < 10 else True if x > 10 else 0
val = False if x < 10 else (True if x > 10 else 0)


# === for ===
# unlike other languages where they give you the control over the iteration
# in python the iteration is done in the order of the sequence

words = ['cat', 'mouse', 'dog']

# iterate through words
for w in words:
    print(w, len(w))

# range function returns a iterable that can be used to iterate (it doesn't create a list - space saver)
range(5) # returns range(0, 5)

# consumes the iterable by summing it
sum(range(5)) # 10

# to actually create a range
list(range(5)) # [0, 1, 2, 3, 4]

for i in range(5):
    print(i) # 0,1,2,3,4

for i in range(1, 5):
    print(i) # 1,2,3,4

# iterate through words using index
for i in range(len(words)):
    print(i, words[i])

# break, else and continue

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'is not a prime number')
            break # won't execute the else
    else:
        # executed when loop is finished without break
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)


# === pass ===
# does nothing
def some_function():
    pass # remember to implement


# === try/catch ===
try:
    x = 1 / 0
expect ZeroDivisionError:
    print('Can divide by 0')
    raise # raise the same exception
expect (TypeError, RuntimeError) as err:
    print('Strange error:', err)
else:
    print('No error =)')
finally:
    print('Always runs')

# We can catch subclass of Exception
class A(Exception):
    pass

try:
    raise A()
expect A:
    print('Error A was thrown')
