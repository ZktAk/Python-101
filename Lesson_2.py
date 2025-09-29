"""Lesson: Loops and Conditionals"""

# -------------------------
# IF / ELIF / ELSE
# -------------------------

"""
Conditionals let your program make decisions based on True/False tests.

if      -> runs only if condition is True
elif    -> runs if the previous if/elif was False, but this is True
else    -> runs if all above conditions are False
"""

temperature = 25

if temperature > 30:
    print("It is hot outside!")
elif temperature > 20:
    print("It is a nice day.")
else:
    print("It is a bit chilly.")

# -------------------------
# WHILE LOOPS
# -------------------------

"""
A while loop repeats as long as a condition is True.
Be careful — if the condition never becomes False, the loop runs forever!
"""

count = 0

while count < 5:
    print(f"Count is {count}")
    count += 1  # Increase count by 1 each time

print("While loop finished!")

# -------------------------
# FOR LOOPS WITH RANGE()
# -------------------------

"""
for loops let you repeat code a fixed number of times.
range(n) generates numbers from 0 to n-1.
"""

for i in range(5):
    print(f"For loop iteration {i}")

print("For loop finished!")

# -------------------------
# LOOPING THROUGH LISTS
# -------------------------

fruits = ["apple", "banana", "cherry"]

# Option 1: Loop directly over items
for fruit in fruits:
    print(f"I like {fruit}")

# Option 2: Loop with index
for i in range(len(fruits)):
    print(f"Fruit #{i}: {fruits[i]}")

# -------------------------
# BREAK AND CONTINUE
# -------------------------

"""
break    -> stops the loop completely
continue -> skips to the next iteration of the loop
"""

for num in range(1, 10):
    if num == 5:
        print("Breaking the loop at 5")
        break  # Exit loop entirely
    elif num % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {num}")

# -------------------------
# NESTED LOOPS
# -------------------------

"""
You can put loops inside other loops.
This is useful for working with grids, patterns, etc.
"""

for row in range(3):  # Outer loop
    for col in range(3):  # Inner loop
        print(f"Row {row}, Column {col}")

# -------------------------
# COMBINING LOOPS AND IF STATEMENTS
# -------------------------

"""
Loops + if statements are powerful together!
Here we print whether each number is even or odd.
"""

for number in range(1, 6):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
