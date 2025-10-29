


firstNumber = input("Input the first number")
secondNumber = input("Input the second number")
operation = input("What operation do you want to carry out (+, -, /, *):")


# Perform the calculation
if operation == "+":
    result = firstNumber + secondNumber
elif operation == "-":
    result = firstNumber - secondNumber
elif operation == "*":
    result = firstNumber * secondNumber
elif operation == "/":
    if secondNumber != 0:
        result = firstNumber / secondNumber
    else:
        result = "Error: Division by zero!"
else:
    result = "Invalid operation!"


print(f"The result is {result}")





