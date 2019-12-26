# Enumerables and Streams

# === Enumarables ===
# Elixir provides the Enum module with functions to
# enumerables manipulations: transform, sort, group, filter an retrieve.
# Those functions are eager and usually returns a list.

Enum.map(1..3, fn x -> x * 2 end)
Enum.reduce(1..3, 0, &+/2)

# question mark is a convention to indicate that it returns a boolean
odd? = &(rem(&1, 2) != 0)
Enum.filter(1..3, odd?)


# each Enum function will return a new list
Enum.sum(Enum.filter(Enum.map(1..100_000, &(&1 * 3)), odd?))

# |> is the pipe operator, takes the output from the left side and use as input
# to the right side

# each step of the pipeline will still return a new list
total_sum = 1..100_000 |> Enum.map(&(&1 * 3)) |> Enum.filter(odd?) |> Enum.sum


# === Streams ===
# Stream module supports lazy operations

total_sum = 1..100_000 |> Stream.map(&(&1 * 3)) |> Stream.filter(odd?) |> Enum.sum

# will only be invoked when passed to a Enum function
odd_numbers_stream = 1..100_000 |> Stream.map(&(&1 * 3)) |> Stream.filter(odd?)

# takes the first 100th numbers
odd_numbers = Enum.take(odd_numbers_stream, 100)

# Create an infinite stream from a cycled list
infinite_stream = Stream.cycle([1, 2, 3])
first_10th = Enum.take(infinite_stream, 10)


# Generate values from a initial value
hello_stream = Stream.unfold("hełło", &String.next_codepoint/1)
Enum.take(hello_stream, 3)
