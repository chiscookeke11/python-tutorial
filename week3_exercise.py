# Task 1
def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False

print(large_power(10, 3))




# Task 2
def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

print(divisible_by_ten(20))
print(divisible_by_ten(33))