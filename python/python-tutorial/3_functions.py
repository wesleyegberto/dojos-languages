#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Functions

my_global = 10

def func_name():
    """
    docstring to document the function.
    A function always returns a value. If we don't return the compile will introduce `None`.
    """
    my_global = 42
    return 42

print(func_name)
new_var = func_name
print(new_var)

print(func_name())


# === Default values ===
def ask_ok(prompt, retries=3, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid response')
        print(reminder)

ask_ok('Did you like?')
ask_ok('OK to overwrite the file?', 2) # prompt and retries
ask_ok('Quit?', 1, 'Please insert Y/N!') # prompt, retries and reminder

# default value is evaluated at the point of function definition
# when the default value is a mutable object calling multiple times might have side effects
i = 5
def f(arg=i):
    print(arg)

i = 6
f() # prints 5

def g(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# secure way
def g_nice(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# === Keyword Arguments ===
def long_function(first, second=2, third=3, fourth=4):
    print("First: ", first)
    print("Second: ", second)
    print("Third: ", third)
    print("Fourth: ", fourth)

long_function(1)
# we can send in another other
long_function(1, third="3333")
# after first named argument, we must keep naming
long_function(1, second="22222", fourth='444444')


# === Special parameters ===
# we can used `**` in the last parameter to receive a map with the keyword arguments that doesn't match
def print_fields(kind, **fields):
    print('Type: ', kind)
    print('Fields:')
    for key in fields:
        print(key, ":", fields[key])

print_fields('User', name='John Doe', age=42)

