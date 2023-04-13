# %% [markdown]
# # CECS 229 Sample Assignment: Python Review
# 
# #### Due Date: 
# 
# January 22nd, 2023
# 
# #### Objectives:
# 
# 1. Review Python functions and classes.
# 2. Know how to convert an .ipynb file to .py
# 3. Understand how to submit work to and read feedback given by, CodePost.
# 
# ### Directions 
# 
# Complete the programming problems below.  When you are finished, convert your notebook to a .py file named `sample.py` and submit it to the appropriate CodePost auto-grader folder.  Please note that this assignment is for practice only and does not affect your grade.
# 
# Review on functions and classes are provided at the end of this notebook for your reference.

# %% [markdown]
# -----------------------------------
# #### Problem 1:
# 
# Create a function `hello(subject)` that returns the string “Hello, (insert subject here)!” using the input subject.
# 
# INPUT: `subject` - a string representing the subject to include in the greeting
# 
# OUTPUT: the greeting as a string

# %%
def hello(subject):
    # Solution
    print(f"Hello, {subject}!") 
    return 
    # or return f"Hello, {subject}!"

# %%
hello("World")

# %% [markdown]
# ----------------------------------------------------------------------------
# #### Problem 2
# 
# Create a class named `Bug` with the following attributes and interface implementation:
# 
# * **Attributes:**
#     - `name` – a string representing the name of this `Bug` object.
#     - `position` – a list with two elements, representing the location of the Bug object on the xy-plane.  The first element represents the x-coordinate, while the second element represents the y-coordinate.
# * **Interface:**
#     - `__init__(self, name, position = [0, 0])`: constructor that initializes a Bug object with given name and position.  If the position is not given, then the Bug’s position is initialized at the origin.
#     - `move_up(self, units)`: moves the position of this Bug object up by given number of units (int).
#     - `move_down(self, units)`: moves the position of this Bug object down by given number of units (int).
#     - `move_left(self, units)`: moves the position of this Bug object left by given number of units (int).
#     - `move_right(self, units)`: moves the position of this Bug object right by given number of units (int).
#     - `__str__(self)`: returns a string representation of this Bug object containing the name and position.  The string should be formatted as follows:
#                 Name: <insert name here>
#                 Position: (<insert x>, <insert y>)
# 

# %%
# Main Program
class Bug():
    # Constructing the Attributes
    def __init__(self, name, position = [0,0]):
        self.name = name
        self.position = position

    # Constructing the Interface
    def move_up(self, units):
        self.position[1] += units

    def move_down(self, units):
        self.position[1] -= units

    def move_right(self, units):
        self.position[0] += units

    def move_left(self, units):
        self.position[0] -= units

    def __str__(self):
        return f"Name: {self.name}\nCurrent Position: ({self.position[1]}, {self.position[0]})"