# Keyword lists and Map

# === Keyword lists ===
# is a list of tuples with two items - O(n)
# characteristics:
#  - key must be atoms
#  - keys are ordered (specified by the developer)
#  - keys can be given more than once

# we can define using common sintax
list = [ { :a, 1 }, { :b, 2 } ]

# or shorthand verson: [ key: value ]
are_equals = list == [ a: 1, b: 2 ]

list ++ [c: 3]
[a: 0] ++ list

# accessing by its key
list[:a] # 0


# if/2 macro uses keyword list
if false, do: :this, else: :that
if(false, [do: :this, else: :that])
if(false, [{:do, :this}, {:else, :that}])

# when a keyword list is the last argument of a function we can omit []

# we can apply pattern match (but the keys must apply - that's why it isn't used so much)
[a: a] = [a: 1]
a # 1


# === Map ===
# Truly key-value store
# characteristics:
#  - allow any value as key
#  - keys do not follow any ordering

map = %{ :a => 1, 2 => :b }
map[:a] # 1
map[2] # :b
map[:c] # nil

# pattern matching is useful (only subset is matched)
%{} = %{ :a => 1, 2 => :b } # %{ :a => 1, 2 => :b }

%{:a => a} = %{ :a => 1, 2 => :b }
a # 1

%{:c => c} = %{ :a => 1, 2 => :b } # error

n = 2
%{^n => nv} = %{ :a => 1, 2 => :b }
nv # :b

a_map = %{ :a => 1, 2 => :b }

# Map module API
Map.get(a_map, :a) # 1
new_map = Map.put(a_map, :c, 3)
Map.to_list(a_map)

# update a key value (key must exists)
%{ a_map | 2 => "two" }

%{ a_map | :c => "error key not found" }


# Map with only atoms as keys can be defined without :
entity = %{ a: 1, b: 2, c: 3 }

# an atom key can be accessed with dot operator
entity.a # strict access (error if not defined)
entity[:a] # dynamic access (nil if not defined)


# macros to update a list of maps
users = [
    odair: %{ name: "Odair Jose", age: 35 }
]

users = put_in users[:odair].age, 36

# update with function
users = update_in users[:odair].age, fn oldAge -> if oldAge < 40, do: 41, else: oldAge + 1 end