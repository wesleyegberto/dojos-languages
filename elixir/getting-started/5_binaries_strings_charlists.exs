# Binaries, strings and Charlits

# === Strings ===
# Elixir uses Unicode stored UTF-8 to encode.

string = "hełło"

# counts the raw bytes
byte_size(string) # 7
# counts the characters
String.length(string) # 5

# get the character's code point
?a # 97

# split the characters
String.codepoints("hełło")


# === Binaries ===
# we use <<>> to define a binary
x = <<0, 1, 2, 3>>
byte_size(x) # 4

# we can check if the binary represents a string
String.valid?(<<333, 222, 19>>)

concat = <<0, 1>> <> <<2, 3>>

# trick to see the string inner bytes representation
"hełło" <> <<0>>

# we can apply match
<<0, 1, x>> = <<0, 1, 2>>
x # 2


# === Charlists ===
# List of code points

'hełło'
is_list 'hełło' # true
List.first('hełło') # 104

to_charlist "hełło"
to_string 'hełło'
to_string :hello
to_string(1)

concat = 'hełło' ++ ' ' ++ 'world'