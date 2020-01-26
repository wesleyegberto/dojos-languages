# Modules - Difinition

# In Python a module is just an importable file .py with some definitions.
# The name of the module will be the filename.
# The modules must be a legal variable name, so this example won't run.

def say_hello():
    print("Hello")

# Will be executed only at first load
print('Module loaded')

# this var should visible inside this module
answer = 42
# but outsiders can access it by: `modulename.var`
