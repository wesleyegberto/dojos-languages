# === Basic Types ===
# integer
# float (64 bits)
# boolean
# atom/symbol: constants whose values is its own name
# string
# list
#   - stored in memory as liked list
#   - length or accessing by index is O(n)
#   - append to tail is O(n) (try to keep append at haed of the elem to add)
# typles:
#   - length or accessing by index is O(1)
#   - update it is slow because always creates a new one

a_int = 2

# float requires a dot followed by at least one digit (.2)
a_float = 1.2
a_float = 1.0e-10 # e notation

a_bool = true

a_atom = :syn
a_bool = a_atom == :syn

# :nil, :true and :false are predefined atoms (we can access without :)
a_bool = true == :true
is_equal = nil == :nil # true


a_str = "Hi"
a_interpolation = "Hello #{:world}"
a_concat = a_str <> " " <> :somewhere_i_belong <> " sufix"
str_length = String.length(a_str) # slow - O(n)
code_points = ?a


a_list = [ 1, 2, 3, 4 ]
a_charlist = 'hello'
mixed_list = [1, 1.1, true, "eita", :ok]
list_length = lengh(a_list) # slow - O(n)
union = [1, 2, 3] ++ [4, 5, 6]
subtraction = [1, 1, 2, 3, 3] -- [1. 3]

[0] ++ a_list # Fast
a_list ++ [0]  # Slow (need to traverse the list)

hd(a_list) # head = 1
tl(a_list) # tail =  [2, 3, 4]


# tuples are immutable
a_tuple = { 1, 2, 3, 4 }
mixed_tuple = { 1, 1.1, true, "eita", :ok }
tuple_size(a_tuple) # returns 4 - fast - O(1)
elem(mixed_tuple, 3) # "eita" - 0-based
new_tuple = put_elem(a_tuple, 3, "new_elem") # replace at index 3

# === Basic Arithmetic ===

# In Elixir, the operator / always returns a float
# to see the table result use in `iex`: `h +/2`
a_float = 10 / 2 # 5.0
a_float = div(10, 2)
a_float = div 10, 2
rest = rem 5, 2

rounded_pi = round(3.14)
truncated_pi = trunc(3.14)



# === Logical Operators ===

## Accept only booleans
both_true = true and is_atom(:should_be)
any_true = false or is_atom(:should_be)
# should_rise_error = 1 and true # BadBooleanError
all_good = false and raise("This will never be raised")
also_good = true or raise("This will never be raised")

not true
not all_good

## Accept anything - only false and nil will be evaluated to false
1 || true # 1
false || 11 # 11

nil && 13 # nil
true && 17 # 17

!true # false
!1 # false
!nil # true

should_be_true = 1 == 1.0
should_be_false = 1 === 1.0
should_be_true = 1 != 1.0 # false
should_be_true = 1 !== 1.0 # true

# type ordering: number < atom < reference < function < port < pid < tuple < map < list < bitstring
1 < :atom # true
