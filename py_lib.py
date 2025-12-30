import math



# Using the math library
print("The square of 36:", math.sqrt(36))
print(math.pi)
print("sine of 90 degrees:", math.sin(math.radians(90)))
print("power of 2^3:", math.pow(2, 3))



# using the random
import random

print("randon number between 1 and 10:", random.randint(1, 10))
print("Random choice from a list:", random.choice(["apple", 'banana', 'cherry']))




# using the datetime library
import datetime

today = datetime.date.today()
print("Today's date is:", today)

now = datetime.datetime.now()
print("Current time:", now.strftime("%H:%M:%S"))