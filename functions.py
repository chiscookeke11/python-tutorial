# Syntax:

def function_name(parameters):
    """Optional docstring explaining the function."""
    # Code block
    return value  # Optional return statement




#     Types of Functions
# Built-in Functions: Predefined functions in Python (e.g., print(), len(), type()).
# User-defined Functions: Functions created by the user.


# Key Components of a Function
# Function Name: Should be descriptive and follow naming conventions.
# Parameters: Variables passed into the function.
# Docstring: An optional description of what the function does.
# Return Statement: Outputs a value from the function (optional).




# Positional arguments
def add(a, b):
    return a + b

print(add(3, 5))



# Default arguments
def greet(name = "guest"):
    return f"Hello {name}"

print(greet())
print(greet("Chinedu"))



# Keyword Arguments:
def introduce(name, age):
    return f"My name is {name}, and I'm {age} years old."

print(introduce(age=25, name="Bob"))



# ANONYMOUS FUNCTIONS: using the "lambda" keyword
add = lambda x, y : x + y
print(add(3, 10))


# using lambda with map
numbers = [1, 3, 5, 6]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)





# Recursive functions
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n -1)

print(factorial(5))