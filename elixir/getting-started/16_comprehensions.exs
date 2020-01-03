# Comprehensions
# Syntact sugar for constructs: loop over an Enumerable, filtering and mapping values into another list.
# A comprehension is made of 3 parts: generators, filters and collectables.

# Map a list of integers into their squared values
for n <- [1, 2, 3, 4], do: n * n


# === Generators and Filters ===
# The expression `n <- [1, 2, 3, 4]` is a generator, any enumerable can be used.

# The following comprehensions are the same:
for n <- [1, 2, 3, 4], do: n * n
for n <- 1..4, do: n * n

# we can use pattern matching to filter a keyword list
values = [good: 1, good: 2, bad: 3, good: 4]
for {:good, n} <- values, do: n * n

# we can use lambdas to filter the elements (false or nil will discard the element)
multiple_of_3? = fn(n) -> rem(n, 3) == 0 end
for n <- 0..5, multiple_of_3?.(n), do: n * n

# we can use multiples generators and filters
dirs = ['/home/johndoe', '/home/joanadoe']
for dir <- dirs, # generator
        file <- File.ls!(dir), # generator
        path = Path.join(dir, file), # generator
        File.regular?(path) do # filter
    File.stat!(path).size
end


# === Bitstring Generators ===
# Are also supported

pixels = <<213, 45, 132, 64, 76, 32, 76, 0, 0, 234, 32, 15>>
for <<r::8, g::8, b::8 <- pixels>>, do: {r, g, b}

for <<c <- " hello world ">>, c != ?\s, do: <<c>>


# === `:into` option ===
# Instead of returning a new list we can feed an existing one.
# It accepts: Set, Map, dictionaries and any structure that implements `Collectable` protocol.

for <<c <- " hello world ">>, c != ?\s, into: "", do: <<c>>

# common case is transforming values in map without touching the keys
for {key, val} <- %{"a" => 1, "b" => 2}, into: %{}, do: {key, val * val}

# streaming the input to output transforming the values
stream = IO.stream(:stdio, :line)
for line <- stream, into: stream do
    String.upcase(line) <> "\n"
end