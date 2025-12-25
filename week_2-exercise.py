# Task 1

# ask the user how many numbers they want to enter
# n = int(input("How many numbers do you want to enter?"))

# numbers = []


# # collect integers from the user
# for i in range(n):
#     value = int(input(f"Enter integer {i + 1}: "))
#     numbers.append(value)


#     # compute the total sum
#     total_sum =  sum(numbers)


# print("The list of integers is:", numbers)
# print("The sum of the integers is:", numbers)






# Task 2
favourite_books = ['Maths', 'Chem', 'Physics', 'Code', 'Speaking']

for book in favourite_books:
    print("My favourite:", book)





# Task 3
# Created an empty dictionary first
person = {}

# Ask the user for the input
# person["name"] = input("Enter your name:")
# person["age"] = int(input("Enter your age:"))
# person["favourite_color"] = input("Enter your favourit color:")


# # print the dictionary
# print("Person information ")
# print(person)



# Task 4
# Ask the user how many elements for each set
# n1 = int(input("How many integers in the first set? "))
# n2 = int(input("How many integers in the second set? "))

# set1 = set()
# set2 = set()

# # Get elements for the first set
# for i in range(n1):
#     value = int(input(f"Enter integer {i + 1} for the first set: "))
#     set1.add(value)

# # Get elements for the second set
# for i in range(n2):
#     value = int(input(f"Enter integer {i + 1} for the second set: "))
#     set2.add(value)

# # Find common elements
# common_elements = set1.intersection(set2)

# print("\nFirst set:", set1)
# print("Second set:", set2)
# print("Common elements:", common_elements)





# Task 5
# list of words
words = ["run", "fight", "matrix", "jump"]

# list comprehension to get words with odd numbers of characters
odd_length_words = [word for word in words if len(word) % 2 != 0 ]

print("Original list:", words)
print("Words with odd numbers of characters:", odd_length_words)
