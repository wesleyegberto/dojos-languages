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

