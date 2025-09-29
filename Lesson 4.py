"""Lesson: Importing Modules and Using Classes"""

# -------------------------
# IMPORTING MODULES
# -------------------------

"""
You can use code from other files or libraries by importing them.
This is called "importing a module."

A module can contain:
- Classes (like turtle.Turtle)
- Functions
- Variables
- Or even other modules!

Here we import the 'turtle' module, which lets us draw graphics
with a "turtle" that moves around the screen.
"""

import turtle

# -------------------------
# CREATING AN OBJECT
# -------------------------

"""
To use a class from a module, create an OBJECT (an instance of the class).

Here we create an object named 'jerry' using turtle.Turtle().
This runs the class constructor (similar to __init__) and returns a new turtle object.
"""

jerry = turtle.Turtle()

# -------------------------
# USING OBJECT METHODS
# -------------------------

"""
Objects have methods (functions inside the class) and attributes (data stored inside the object).

Here we use methods to control our turtle's behavior:
- speed() sets how fast the turtle moves (0 is fastest).
- color() sets the turtle's drawing color.
"""

jerry.speed(0)           # 0 = "no animation" (fastest)
jerry.color("#2F4F4F")   # Dark Slate Gray color

# -------------------------
# BEGIN DRAWING
# -------------------------

"""
begin_fill() starts filling any shape we draw after this point.
We'll call end_fill() when we're done drawing to actually fill the shape.
"""

jerry.begin_fill()

# -------------------------
# MATH FOR DRAWING
# -------------------------

"""
These formulas calculate:
- side_length: how far the turtle moves forward each time
- iterations: how many times the loop runs

You can tweak 'x' to change the pattern!
"""

x = 3
side_length = float((2.08333 * pow(x, 3)) + (-26.25 * pow(x, 2)) + (101.667 * x) - 110)
iterations = int((-11.25 * pow(x, 3)) + (446.25 * pow(x, 2)) + (-2707.5 * x) + 4770)

print("Drawing: Ornate Flower Shuriken Mosaic")

# -------------------------
# DRAWING LOOP
# -------------------------

"""
This loop repeats 'iterations' times.
Each iteration:
1. Moves the turtle forward by 'side_length'
2. Rotates the turtle left by (1 + (count^x % 360)) degrees

This creates a complex, rotating pattern.
"""

for count in range(iterations):
    jerry.forward(side_length)
    jerry.left(1 + pow(count, x) % 360)

# End filling after the loop
jerry.end_fill()

# -------------------------
# KEEP THE WINDOW OPEN
# -------------------------

"""
Wait for user input before closing the window, so you can admire your creation.
"""

answer = input("Please enter 'd' when done: ")
