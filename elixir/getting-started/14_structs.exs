# Structs

# Structs are extensions built on top of maps that provide compile-time checks
# and default values.

defmodule User do
    # structs take the name of its module
    # we can define a default value or `nil` will be assumed
    defstruct [:name, age: 42]
end

%User{}

odair = %User{name: "Odair Jose"}

# is a bare map underneath
is_map(odair)

# bare because it doesn't implement the maps' protocols
# we cannot use this syntax
# odair[:name]

# we cannot use enumeration
# Enum.each odair, fn({field, value}) ->  IO.puts(value) end

# But we can use the Map module
Map.merge(odair, %User{name: "New Name"})

Map.keys(odair)


# special field with the name name of the struct
odair.__struct__

# will generate an compile error
# %User{notDefined: :field}

me = %User{name: "Wesley"}


me.name

# olderMe will share the same key structure in memory
olderMe = %{me | age: 43}



defmodule Hero do
    # we can enforce the keys that must be specified when creating
    @enforce_keys [:power]
    defstruct [:secretName, :power]
end

# Error: the following keys must also be given when building struct Car: [:make]
# %Hero{}

%Hero{power: :fly}
