
#       (      MODULES AND PACKAGES                   )


# modules and packages are the core tools used to organize, scale, and reuse code

# ==========================================
#               1. What is a Package?

# A package is a directory (folder) that groups related modules together. 
# Packages allow you to structure multi-file

# my_project/
# │
# ├── main.py                 # The script you run
# └── my_package/             # The package folder
#     ├── __init__.py         # Marks this folder as a package
#     ├── geometry.py         # Submodule 1
#     └── algebra.py          # Submodule 2



#                How to use a Package??



#  main.py

# Option 1: Import the whole submodule
import my_package.geometry
print(my_package.geometry.calculate_area(5))

# Option 2: Import a specific function from a submodule
from my_package.algebra import solve_equation
print(solve_equation(x=2))


# # ===================================================================

#                     2. What is a Module?

#  module is simply any Python file ending in .py. 
# It can contain functions, classes, and variables
# that you want to use across different scripts. 


# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# ==============================

