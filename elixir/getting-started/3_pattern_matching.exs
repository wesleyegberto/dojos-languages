# === Pattern Matching ===
# = is actually a match operator
# ^ is a pin operator (enforce the use of match operator)

# assign to a variable (left side)
x = 1

1 = x

# 2 = x # raise an error (no match)


# === Tuples ===
# destructuring complex data types
{ a, b, c } = { :hello, "world", 42 }

# error: missing one element at matching
# { a, b, c } = { "raising", "error" }

# will only match if the tuple start with same value
{ :ok, result } = { :ok, 13 }

# error: no matching
# { :ok, result } = { :error, "Some error" }


# === Lists ===
# error: no match of right hand side value (different types)
# { a, b, c } = [ :hello, "wolrd", 42 ]
[ a, b, c ] = [ "hello", :word, 42 ]

# matching head and til
[ listHead | listTail ] = [ 1, 2, 3 ]
listHead # 1
listTail # [ 2, 3 ]

# error: no matching at right side
# [ head | tail ] = []

# we can create using head tail
a_list = [ 1, 2, 3 ]
new_list = [ 0 | a_list ]


# === Pin Operator ===
x = 1 # assign
x = 2 # assign

# ^ enforces the matchs (avoiding the assignment of a value)
^x = 1 # matches
^x = 2 # error: no match

{ y, ^x } = { 2, 1 } # matches
{ y, ^x } = { 2, 2 } # error: no match

# when referencing more than once all values should be the same
{ x, x } = { 1, 1 }
{ x, x } = { 1, 2 } # error

# Functions cannot be used at left hand of the match operator
# length([1, 2 ,3]) = 3
3 = length([1, 2 ,3])


# === _ Operator ===
# used to ignore some value
[ head | _ ] = [ 0, 1, 2 ]
head # 0
# _ wont be even assigned
