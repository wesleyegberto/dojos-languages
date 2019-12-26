# alias, require and import

# All modules defined in Elixir namespace
# `List.first/1` is fully-qualified as `Elixir.List.first/1`


# === alias ===
# allows to set up aliases for modules.
# is lexically scoped, allowing to set alias inside a specific function

alias Foo.Bar, as: Bar
alias Foo.Bar # will be aliased as Bar (last part of name)
Foo.Bar.doStuff
Bar.doStuff

# During compilation, the alias is converted to an atom (because in the Erlang VM modules are always
# represented by atoms)
alias String, as: Test
:"Elixir.String" == String
Test == String
Test == :"Elixir.String"
Test == Elixir.String


# === require ===
# Elixir provides macros as a mechanism for meta-programming, macros are expanded at compile time.
# Public function in modules are globally available, but to use macros we need to opt-in by requiring it.
# require the module to use its macros (like guards)

# provides macros to use in guards
require Integer
Integer.is_odd(3)


# === import ===
# import functions to access its functions or macros without using the prefix

Foo.doSomething # before import
import Foo # import all functions
doSomething


import Foo, only: [doSomething: 0] # only doSomething/0 function
import Foo, except: [doSomething: 0] # expect doSomething/0 function


# === use ===
# Used as an extension point.
# When using a module we allow that module to inject any code (importing modules, define new functions,
# setting a module state) in the current module.
# Since use allows any code to run we can't really know the side-effects of using a module without reading
# its documentation. For this reason, `import` and `alias` are often preferred.

# Behind the scenes, `use` requires the given module and then call the `__using__/1` callback on it.
defmodule Example do
  use Feature, option: :value
end

# is compiled into
defmodule Example do
  require Feature
  Feature.__using__(option: :value)
end

# Example:
defmodule AssertionTest do
    # use and apply all code from ExUnit.Case
    use ExUnit.Case, async: true

    test "always pass" do
        assert true
    end
end



# === Multi ===
# From Elixir v1.2 we can refer to multiple modules ate once.
alias MyModule.{Foo, Bar, Baz}
use MyModule.{Foo, Bar}
