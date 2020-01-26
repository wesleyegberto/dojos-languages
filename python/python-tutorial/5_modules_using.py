# Modules - Using

# we just need to import the file to use the module
import 5_modules_difinition
5_modules_difinition.say_hello()

# we can only import the functions we gonna use
from 5_modules_difinition import say_hello
from 5_modules_difinition import *
say_hello()

# we can set a aliase
import 5_modules_difinition as md
md.say_hello()

# accessing its global vars (not recommended)
md.answer
