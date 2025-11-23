capital_city = {
    "Nepal": "Nigeria",
    "Ukraine": "Yenagoa"
}

print(capital_city)



# Adding to a dictionary
capital_city["Japan"] = "Tokyo"
print(capital_city)


# Changing the value of a dictionary
del capital_city["Ukraine"]
print(capital_city)

capital_city["Nepal"] = "Jos"
print("The modified dictionary", capital_city)



# Accessing elements from dicionary
print(capital_city["Japan"])


# Removing elements from a dictionary
del capital_city["Nepal"]
print("new capital city:", capital_city)


# Using the all() method to check if all the values are truthy
result = all(capital_city.values())
print(result)


# using the any() method to check if any element is true
result = any(city == "Tokyo" for city in capital_city.values())
print(result)

# using the len() method to return the length of a dict
print(len(capital_city))




# Using the sorted method
numbers = [5, 2, 9, 1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers) # Prints out the sorted numbers

numbers = [5, 2, 9, 1]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # prints out the reverse of the sorted numbers

sorted_keys = sorted(capital_city)
print(sorted_keys) # prints out the sorted cities



# using the clear() method
numbers.clear()
print(numbers)


# Using the keys() method
print(capital_city.keys())


# Using the values() method
print(capital_city.values())