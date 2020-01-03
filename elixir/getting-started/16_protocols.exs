# Protocols

# Protocols are a mechanism to achieve polymorphism in Elixir.
# we can define for all types:
# - Atom
# - BitString
# - Float
# - Function
# - Integer
# - List
# - Map
# - PID
# - Port
# - Reference
# - Tuple


# === Simple Types ===

# definition
defprotocol SayHello do
  @doc "Say hello to something"
  def hello(data)
end


# Implementations

defimpl SayHello, for: Integer do
    def hello(number), do: IO.puts("Hello number, #{number}")
end

defimpl SayHello, for: BitString do
    def hello(string), do: IO.puts("Hello string, #{string}")
end

SayHello.hello(42)

SayHello.hello("Text")


# === Structs ===
# Even though structs are maps, they do not share protocol implementations.
# Structs require their own protocol implementation.
defprotocol KeysCounter do
    @doc "Counts the fields quantity"
    def count(map)
end

defimpl KeysCounter, for: Map do
    def count(map), do: map_size(map)
end

# Counting maps fields
IO.puts KeysCounter.count(%{})
IO.puts KeysCounter.count(%{name: "Odair"})

# Error: protocol KeysCounter not implemented for #MapSet<[]> of type MapSet (a struct)
# IO.puts KeysCounter.count(MapSet.new)

# to demonstrate, MapSet is implemented as structs
defimpl KeysCounter, for: MapSet do
    def count(mapSet), do: MapSet.size(mapSet)
end

IO.puts KeysCounter.count(MapSet.new)
IO.puts KeysCounter.count(%MapSet{})

# another struct could't use MapSet protocol implementation
defmodule User do
    defstruct [:name, :age]
end

john = %User{name: "John Doe"}

# Error: protocol KeysCounter not implemented for %User{age: nil, name: "John Doe"} of type User (a struct)
# IO.puts KeysCounter.count(john)

defimpl KeysCounter, for: User do
    def count(mapSet), do: 2 # 2 fields
end

IO.puts KeysCounter.count(john)


# === Implemeting `Any` ===
# we can implement a protocol using for `Any` to be used as fallback when a type doesn't have an implementation.

# fallback implementation
defimpl KeysCounter, for: Any do
    def count(_), do: 0
end

## Using `@derive`
# Elixir will implement the protocol based on `Any` implementation
# we must do this for each new struct
defmodule Object do
    @derive [KeysCounter]
    defstruct [:name, :weight]
end

IO.puts KeysCounter.count(%Object{})

## Using `@fallback_to_any`
# We can mark a protocol to fallback to `Any` to all types when there isn't a specific implementation.
defprotocol ValuesMerger do
    @doc "Merge the values of the given type"
    @fallback_to_any true
    def merge(type)
end

defimpl ValuesMerger, for: Any do
    def merge(_), do: 0
end

# even though the struct User does not implement or declare @derive it will call any
IO.puts ValuesMerger.merge(john)