# === Modules and Functions ===
# use defmodule macro to create a module
# to compile: `elixirc 7_modules.ex`
# the beam file contains the bytecodes
# when running `iex` it will automatically load the beam files

defmodule MyMath do
    def sum(a, b) do
        do_sum(a, b)
    end

    # Private function (only accessible inside this module)
    defp do_sum(a, b) do
        a + b
    end

    # the question mark is a convention to
    # indicate that it returns a boolean
    def zero?(0) do
        true
    end

    # short version using do:
    # def zero?(0), do: true

    # we can use guards in functions
    def zero?(x) when is_integer(x) do
        false
    end

    # short version using do:
    # def zero?(x) when is_integer(x), do: false
end

defmodule Concat do
    # we can set default argument using \\
    # everytime the function is invoked the argument
    # expression will be evaluated
    def join(a, b, sep \\ " ") do
        a <> sep <> b
    end

    # if a function with default values has multiple clauses, it
    # is required to create a function head
    def join_2(a, b \\ nil, sep \\ " ")

    # underscore in _sep means that the var will be ignored
    def join_2(a, b, _sep) when is_nil(b) do
        a
    end

    def join_2(a, b, sep) do
        a <> sep <> b
    end
end

IO.puts MyMath.sum(1, 2)


IO.puts Concat.join("hello", "world")
IO.puts Concat.join("hello", "world", "_")

# === Function Capturing ===
# we can use name/arity to refer to a function
# using capture operator &

func = &Math.zero?/1
is_function(func)
fun.(0) # true

# captures is_function and invoke it
(&is_function/1).(fun)


# We can also use capture syntax as shortcut for creating function
func = &(&1 + 1) # &1 is the first argument
# func = fn x -> x + 1 end # long version
func.(1) # 2

func_2 = &"Good #{&1}"
func_2.("morning")

func = &List.flatten(&1, &2)
# func = fn(list, tail) -> List.flatten(list, tail) end # long version
func.([1, [[2], [3]]], [4, 5])


# === Nesting Module ===
defmodule Foo do
    defmodule Bar do
        def doStuff do
        end
    end
    # here we can use Bar.doStuff
end
# here we use Foo.Bar.doStuff