"""Lesson: Functions, Classes, and Objects"""

# -------------------------
# FUNCTIONS
# -------------------------

"""
Functions let you group code into reusable blocks.
You can pass data into functions using parameters,
and get data out using return values.
"""

# Example of defining a simple function
def add(a, b):
    """Takes two numbers and returns their sum."""
    result = a + b
    return result

# Using the function
x = add(4, 2)
print(x)  # Output: 6

# -------------------------
# CLASSES & OBJECTS
# -------------------------

"""
Classes let you group data (attributes) and behavior (methods) together.
You can then create objects (instances) of that class.
"""

class MyClass:
    """A simple example class with one attribute and one method."""

    def __init__(self, val):
        """
        The __init__ method is the class constructor.
        It runs automatically when you create an object.
        'self' represents the object being created.
        """
        self.my_value = val  # Attribute: stores data inside the object

    def subtract(self, x):
        """
        A method that uses the object's stored value (self.my_value)
        and subtracts x from it.
        """
        return self.my_value - x

# -------------------------
# USING CLASSES
# -------------------------

"""
To use a class, you create an object (instance) from it.
You can then call its methods just like a function.
"""

# Create an object from MyClass with my_value = 5
subtractor = MyClass(5)

# Call its subtract method
x = subtractor.subtract(2)
print(x)  # Output: 3
