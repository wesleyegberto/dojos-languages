# === Basic Functions ===
# Funcion is identified by its name and the number of arguments it takes (arity)

## Predicate Functions (to check types)
is_boolean(true)
is_integer(1)
is_float(1.0)
is_number(1)
is_atom(:syn)
is_function(a_function)
is_binary("hello")
byte_size("hello")

## IO
IO.puts "A simple string to print at console"


# === String functions ===
String.length("give me my size") # slow - O(n)
String.upcase("transform to upper case")


# === Anonymous functions ===
add = fn a, b -> a + b end
add.(1, 2) # use .() to invoke it (and eliminate the ambiguity between anonymous and add/2)
add(1, 2) # would call a defined named function

# as function are also closure we can access vars in scope
# (readonly - even if we change inside it wont have any effect outside)
double = fn a -> add.(a, a) end #

# is_function also check its arity
is_function(add, 2) # true
is_function(add, 1) # false
