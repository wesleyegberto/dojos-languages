# Recursion

# === Loop through recursion ===
defmodule Recursion do
    def print_multiple_times(msg, n) when n <= 1 do
        IO.puts msg
    end

    def print_multiple_times(msg, n) do
        IO.puts msg
        print_multiple_times(msg, n - 1)
    end
end

Recursion.print_multiple_times("Hi", 3)


# === Reduce and Map ===
# Recursion and tail call optimization are an important part of Elixir
# and are commonly used to create loops.

defmodule ListMath do
    def sum_list([head | tail], accumulator) do
        sum_list(tail, head + accumulator)
    end

    def sum_list([], accumulator) do
        accumulator
    end

    def double_each([head | tail]) do
        [head * 2 | double_each(tail)]
    end

    def double_each([]) do
        []
    end
end

ListMath.sum_list([1, 2, 3], 0)

ListMath.double_each([1, 2, 3])


# To manipulate list we will commonly use Enum
Enum.reduce([1, 2, 3], 0, fn(x, acc) -> x + acc end)
Enum.reduce([1, 2, 3], 0, &+/2)

Enum.map([1, 2, 3], fn(x) -> x * 2 end)
Enum.map([1, 2, 3], &(&1 * 2))
