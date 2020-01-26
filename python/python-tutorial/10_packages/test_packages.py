# In Python, packages can be used to organize the modules, avoding conflicts between libs.

# Every folder must contain a file `__init__.py` to Python treats it as a package.

# from package_a.subpackage_a import a_module
from package_a.subpackage_a import *

a_module.do_stuff()
