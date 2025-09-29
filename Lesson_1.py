"""Lesson 1: Python Basics"""

# -------------------------
# COMMENTS
# -------------------------

# This is a single-line comment. Use the '#' symbol to write notes for yourself or others.
# Python ignores these lines when running your program.

"""
This is a docstring (triple double quotes).
It can span multiple lines and is often used at the start of a file,
class, or function to describe what it does.
"""

# TIP: Always use triple double quotes ( """ ) for block comments.

'''
This looks similar, but it is actually a string literal, NOT a comment.
Avoid using triple single quotes for comments.
'''

# -------------------------
# PRINT STATEMENT
# -------------------------

"""
The print() function is used to display output on the screen.
You can print text, numbers, or a mix of both.
"""

# print("Hello World!")
# print('Have a nice day!')
# print(2022)

# -------------------------
# ESCAPE CHARACTERS
# -------------------------

"""
Escape characters let you include special formatting in strings.
Examples:
- \n  -> New line
- \t  -> Tab space
- \"  -> Double quote inside a string
Uncomment the follow code lines to see how they work
"""

# print("Hello \nWorld")   # New line
# print("\"Hello World\"") # Prints "Hello World" with quotes
# print("\tHello World")   # Tab before "Hello"

# -------------------------
# VARIABLES
# -------------------------

"""
Variables store data that you can use later.
You do not need to declare a type — Python figures it out for you.
"""

x = "Hello Awesome World!"
print(x)  # Prints the string value

x = 2022  # You can reuse the same variable name with a different type
print(x)  # Prints a number

# -------------------------
# USER INPUT
# -------------------------

"""
Use input() to get data from the user.
The program will pause and wait for input.
"""

# x = input("Please type a message: ")
# print(x)

# -------------------------
# DATA TYPES
# -------------------------

"""
Common Python data types:
- str (string)  : "Hello"
- int (integer) : 10
- float        : 3.14
- complex      : 1j
- list         : ["apple", "banana"]
- tuple        : ("apple", "banana")
- bool         : True / False
- NoneType     : None (represents "nothing")
"""

# Strings
x = "Hello World"  # str
# print(x)

# Numbers
x = 20  # int
x = 20.5  # float
x = 1j  # complex

# Lists (mutable — you can change them)
x = ["apple", "banana", "cherry"]
# print(x)

x.append("grape")  # Adds an item to the end
# print(x)

x[0] = "orange"  # Changes the first item
# print(x[0])

# Tuples (immutable — you cannot change them)
x = ("apple", "banana", "cherry")

# Booleans
x = True
x = False

# print(9 == 10)  # False
# print(10 > 9)   # True

# NoneType
x = None

# -------------------------
"""Lesson 2: More Basics"""
# -------------------------

# TYPE CASTING (Converting data types)

# print(int(2.8))       # Converts float to int (drops decimal)
# print(int("3"))       # Converts string to int

# print(float(1))       # Converts int to float
# print(float("3.5"))   # Converts string to float

# print(str(2.8))       # Converts number to string

# -------------------------
# STRING OPERATIONS
# -------------------------

# x = "hello world"
# print(x[6])       # Access a single character (index starts at 0)
# print(len(x))     # String length
# print(x[1:5])     # Slice (characters 1 to 4)
# print(x[:5])      # From start to index 4
# print(x[6:])      # From index 6 to end
# print(x[-2])      # Second-to-last character

# Combining strings
# a = "Hello"
# b = "World"
# print(a, b)           # Prints with space
# print(a + " " + b)    # Concatenation

# Using format()
# year = 2022
# print("The year is {}".format(year))

# Using f-strings (more common and easier to read)
# print(f"The year is {year}")

# month = "July"
# day = 22
# print("The date today is {} {}, {}".format(month, day, year))

# f-string equivalent
# print(f"The date today is {month} {day}, {year}")

# -------------------------
# LIST OPERATIONS
# -------------------------

x = ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]

# x[5] = "_"_
