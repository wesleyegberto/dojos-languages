# Modules Attributes

# serve three purposes
# - annotate the module, often with info to be used by the user or the VM;
# - work as contants;
# - work as temporary module storage to be used during compilation.

defmodule MyModule do
    # reserved attribute used to versioning
    # by the Earlang VM during the core reloading
    @vsn 2

    # documentation for the current module
    @moduledoc """
    # My Module

    This is a multiline string.
    _We can use markdown syntax_
    """

    # We can use as constants
    @universe_answer 42

    @doc """
    Doc for the function
    """
    def my_function do
        1
    end

    @doc """
    Calculates the answer for the universe
    """
    def calculate_universe, do: @universe_answer
end

# Access the documentation (Elixir treats docs as first-class and provides many functions)
# h MyModule.my_function

# we can use ExDoc to generate HTML pages from the documentation


defmodule Foo do
    # attributes usually override the value, we can change it to accumulate in an array
    Module.register_attribute __MODULE__, :param, accumulate: true

    @param :foo
    @param :bar

    # @param == [:foo, :bar]

    # we can call another function in another module (the current module we cannot)
    @universe_answer MyModule.calculate_universe
end

