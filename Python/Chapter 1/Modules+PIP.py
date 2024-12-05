# Modules + Pip
# Modules in Python are files that contain reusable code. They can include functions, classes, and variables, 
# and you can import them into your program to make use of their functionality.

# To install any of the open source modules, like pyjokes, we use pip, which is the package manager for Python. 
# You can use pip to install modules on your system.
# For example, you can use this line of code (given below) in the terminal to install the module:
# pip install pyjokes

# Now, to execute the installed module, we use the import code as shown below:
import pyjokes
print(pyjokes.get_joke())

# You can also install more modules that are open-sourced, created by other programmers, to test the code on your computer.
# For example, you can install the Flask module by using the following:
# pip install flask

# There are two types of modules in Python:
# 1. External modules: These modules are not pre-installed with Python. 
#    You need to install them manually using pip or another package manager. These modules are created by other programmers or organizations.
# 2. Built-in modules: These modules come pre-installed with Python when you install it on your computer. 
#    They are part of the Python standard library and don't need to be installed separately.