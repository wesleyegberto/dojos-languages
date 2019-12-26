# Control Flow: case, cond, if, unless, do/end blocks

# === case ===

case { 1, 2, 3 } do
    { 4, 5, 6 } -> "This won't match"
    { 1, x, 3 } -> "This will match and bind x to 2"
    _ -> "Default case =)"
end

x = 1
case 10 do
    ^x -> "Won't match"
    _ -> "Will match default case"
end

# we can use guards to specify extra conditions
case { 1, 2, 3 } do
    { 1, x, 3 } when x > 0 -> "Will match because x = 2 and x will > 0"
    _ -> "Won't match"
end

# errors in guard won't be raised
# hd(1) # argument error
case 1 do
    x when hd(x) -> "Won't match nor will raise error"
    x -> "Got #{x}"
end

# when none of clauses match, an error is raised
case :ok do
    :nope -> "Won't match"
    :neither -> "Won't match"
end

# anonymous functions can also have clauses
f = fn
    x, y when x > 0 -> x + y
    x, y -> x * y
end
f.(1, 3) # 4
f.(-1, 3) # -3


# === cond ===
# we use when we need find the first conditions (not nil or false)
# using differents values
# if none matche then a CondClauseError will be raised

cond do
    2 + 2 == 5 -> "Won't be true"
    2 * 2 == 3 -> "Won't be true"
    1 + 1 == 2 -> "Will be true"
    true -> "true condition to avoid error"
end


# === if, unless ===
# if and unless are implemented as macros in the language
if true do
    "This works"
end

unless true do
    "Wont be reached"
end

if nil do
    "Wont be reached"
else
    "This will"
end


# === do/end blocks ===
# short version
if true, do: 1 + 2
if false, do: :error, else: :ok

if true do
    a = 1 + 2
    a + 10
end

if true, do: (
    a = 1 + 2
    a + 10
)

# do/end is always bounded to the outermost function call
# raise error: will look for is_number/2
is_number if true do
    1 + 2
end
# parsed as:
is_number(if true) do
    1 + 2
end

# correct version:
is_number(if true do
    1 + 2
end)

