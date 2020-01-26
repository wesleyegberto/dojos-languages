# === Modules ===

# A module is a importable file `.py`.
# In runtime, Python add a var `__name__` with the name of the module. If the module is running as script the value will be `__main__`.
# The módule can have statements to be executed during its first load.

# hello.py
def say_hello():
    print('Hello!')

print('Module {} loaded'.format(__name__))

# We can use it and access its name:
import hello # nome do arquivo
hello.say_hello()
hello.__name__ # nome do módulo

# We can import only the used members:
from hello import say_hello
say_hello()

# We can define a aliase to the imported module:
import hello as hi
hi.say_hello()

from hello import say_hello as hi
hi()


## === Scopes ===
# Each module has its own symbol table that is only available within the modulee.
# The variables names don't conflict with others, but we still can access its vars by `modulename.itemname`

# util.py
def do_stuff():
    pass
private_flag = 0

# accessing the var
import util
util.do_stuff()
util.private_flag # argh


# === Scripts ===
# We can run a module by `python <filename.py> <arguments>`
# In this case, the module name will be `__main__`.

# util.py    
def do_stuff(var);
    pass

if __name__ == '__main__':
    import sys
    arg = sys.argv[1]
    print("Scripting... {}".format(arg))
    do_stuff(arg)


## === `dir()` function ===

Podemos usar a função dir para saber quais membros um módulo declarou.

import util
dir(util) # prints an array with module members (inclusive __name__, do_stuff)
dir() # prints the members of current module (incluindo `util`)


# === Packages ===
# Package allow us to structure the Python modules in an way to not conflict with others modules.
# We can use dotted module names to import a module.

# my_package/my_subpackage/module.py
def do_stuff():
    pass

# To import it we must use its full name
import my_packag
my_package.my_subpackage.module.do_stuff()

from my_package.my_subpackage import module
module.do_stuff()

from my_package import my_subpackage
my_subpackage.module.do_stuff()

# To Python recognize the folder as a package we need to create a file `__init__.py` in the folder.
# This file will received a variable `__path__` with its complete path.

# Considering the following structure:
# my_package/
#     __init__.py
#     my_subpackage/
#         __init__.py
#         module.py
#     another_subpackage/
#         __init__.py
#         another_module.py

# In order to use import all `*` in a package, the file `__init__py` will need to declare a variable `__all__` with the modules that should
# be imported by default. If it is empty nothing will be imported.

# file: my_package/__init__.py
__all__ = ["my_subpackage"]

# If other module import it using `*` then it will be only import my_subpackage:
from my_package import *
my_subpackage.another_subpackage.do_stuff()


# Intra-package References
# We can import a module/package using relative notation with dots

from .. import my_subpackage.another_package
# ou
from ..my_subpackage import another_subpackage

# importing from the same package
from . import module_2