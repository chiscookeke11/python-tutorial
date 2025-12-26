# In computer programming, loops are used to repeat a block of code. We perform a process of iteration (repeating tasks).



# There are 2 types of loops in Python:

# for loop
# while loop

# Programming languages like Python implement two types of iteration:

# Indefinite iteration, where the number of times the loop is executed depends on how many times a condition is met.
# Definite iteration, where the number of times the loop will be executed is defined in advance (usually based on the collection size).

# In a for loop, we will know in advance how many times the loop will need to iterate because we will be working on a collection with a predefined length.

# With for loops, on each iteration, we will be able to perform an action on each element of the collection.

# Example of a for loop
fruits = ["Apple", "Banana", "Grape"]


for fruit in fruits:
    print(f"I love {fruit}! ")





# For Loops: Using Range

# A range is a series of values between two numeric intervals.

# We use Python's built-in function range() to define a range of values.

# For example,

# five_steps = range(5)

# # five_steps is now a collection with 5 elements:

# # 0, 1, 2, 3, 4

# Example of a for loop with range
for number in range(1, 6):  # Loops from 1 to 5
    print(f"Number: {number}")







    # --------------------------------------------------    While Loop    -------------------------------------------------
    # A while loop performs a set of instructions as long as a given condition is true.

#     While loop structure

# # Example of a while loop
count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1  # Increment the counter






# Loop controls: Break and continue

# The break statement is used to terminate the loop immediately when it is encountered.

# Example of loop controls: break and continue
for number in range(1, 10):
    if number == 5:
        print("Breaking the loop")
        break
    elif number % 2 == 0:
        print(f"Skipping {number} because it is even")
        continue
    print(f"Processing the number: {number}")



#     Nested Loops

# In Python, loops can be nested inside other loops. Nested loops can be used to access items of lists which are inside other lists. The item selected from the outer loop can be used as the list for the inner loop to iterate over.

# Example code

# Example of a nested loop
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"Outer loop: {i}, Inner loop: {j}")