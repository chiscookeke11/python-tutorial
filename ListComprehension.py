
# A list comprehension is a compact syntax for creating a list by evaluating an expression for each element in an iterable (like a list or range), optionally filtering elements based on a condition.

# Syntax:
# [expression for item in iterable if condition]
# expression: The value or transformation applied to each element.
# item: A variable that represents each element in the iterable.
# iterable: A sequence (like a list, tuple, or range) to iterate over.
# condition: (Optional) A filter that determines whether to include the element.



# basic example
# Traditional loop
squares = []
for x in range(5):
    squares.append(x ** 2)


# List Comprehension
squares = [x ** 2 for x in range(5)]

print(squares)




# USING CONDITIONS IN LIST COMPREHENSION
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)



# NESTED LIST COMPREHENSION
# creating a 3 x 3 matrix using nested list comprehensions
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4) ]
print(matrix)



# TRANSFORMING DATA
names = ["chinedu", "john", "micheal"]
uppercased_names = [name.upper() for name in names]
print(uppercased_names)




# FILTERING DATA
NUMBERS = [10, 15, 20, 25, 30]
divisible_by_5 = [num for num in NUMBERS if num % 5 == 0]
print(divisible_by_5)



# FLATTENING A LIST
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)




