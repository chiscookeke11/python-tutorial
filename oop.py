class car:
    color = "red"

    def drive(self):
        print("The car is driving")


my_car = car()
print(my_car.color)
my_car.drive()



# Use python constructors
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model



car1 = Car("blue", "Sedan")
car2 = Car("red", "SUV")



print(car1.color)
print(car2.model)



# OOP inheritance
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels


class Car(Vehicle):
    pass



car = Car(4)
print(car.wheels)



# Polymorphism
class Dog:
    def speak(self):
        return "woof!"


class Cat:
    def speak(self):
        return "Meow!"



for animal in [Dog(), Cat()]:
    print(animal.speak())






# Encapsulation
class SecretStash:
    def __init__(self):
        self._chocolates = 10   # protected attribute

    def take_chocolate(self):
        if self._chocolates > 0:
            self._chocolates -= 1
            print("One chocolate taken!")
        else:
            print("No chocolates left 😢")


stash = SecretStash()
stash.take_chocolate()
stash.take_chocolate()




