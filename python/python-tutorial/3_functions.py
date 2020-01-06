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
# by default we can pass the args by positional, keywords or mixing it
def sample(first, second, third):
    print('First', first)
    print('Second', second)
    print('Third', third)

sample(1, 2, 3)
sample(1, 2, third=3)
sample(1, second=2, third=3)
sample(first=1, second=2, third=3)


## Arguments list to Map: we can use `**` in the last parameter to receive a map with the keyword arguments that doesn't match
def print_fields(kind, **fields):
    print('Type: ', kind)
    print('Fields:')
    for key in fields:
        print(key, ":", fields[key])

print_fields('User', name='John Doe', age=42)
print_fields('Animal', specie='Dog', legs=4, hasTail=True)


## Positional only: we can use slash `/` to mark parameters before it must be passed only by positional
def test_positional(first, second, /):
    print('First param: ', first)
    print('Second param:', second)

# incorrent (must only be positional)
test_positional(1, second=2)
test_positional(second=2, first=1)

# correct
test_positional(1, 2)


## Keyword only: we can use start `*` to mark the parameters to to be passed only by keywords
def test_keywords(*, first, second):
    print('First', first)
    print('Second', second)

# incorrent (must use keyword)
test_keywords(1, 2)
test_keywords(1, second=2)

# correct
test_keywords(first=1, second=2)
test_keywords(second=2, first=1)


# combined
def combined(positional_only, /, positional_or_keyword, *, keyword_only):
    print('Called')


## Arbitrary list: we can use * at a parameter to accept an arbitrary list (they are wrapped in a tuple)
def join_with_space(*args):
    return " ".join(args)


join_with_space("I", "you", "he", "she")
join_with_space("When")

# we can also declare others parameters after it but they must be passed using keyword
def join(*args, sep=","):
    return sep.join(args)

join("I", "you")
join("he", "she", sep="-")

## Unpacking arguments: we can extract the values from list or tuple to pass it as arguments

# Unpacking from a list or tuple using star `*`
# range expect at most 3 params: from, to, step = 1
list(range(1, 4)) # [1, 2, 3]
args = [3, 6]
list(range(*args)) # [3, 4, 5]

# Unpacking from a map using double stars `**`
def sample(first, second):
    pass

map = { "first": 1, "second": 2 }
sample(**map)


# === Lambda ===
# Lambda function is syntactically restricted to a single expression. It can be used wherever expect a function.
summer = lambda x: x + x
multiplier = lambda x, y: x * y

def operate(value, operation):
    return operation(value)

operate(1, summer)
operate(2, lambda x: 2 * x)

