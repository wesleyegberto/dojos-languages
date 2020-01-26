# Even the lowest package should contain the __init__.py

print("package_a.subpackage_a path: ", __path__)

# we can set __all__ to be used when: `from package_a.subpackage_a import *`
__all__ = ['a_module']
