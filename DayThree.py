# Declaring a list
list_a = [1, 2, 34, 565, 7676, 8787, 87878, ]

# accessing the length of a list
lenOfList = len(list_a)
print(lenOfList)


# Accessing a value in the list based on index
print(list_a[3])


#Slicing part of a list with the ":" symbol
midSection = list_a[3:]
print(midSection)


# Adding elements to a list using the append method
list_a.append(32)
print(list_a)

# Adding elements to a list using the extend method
list_b  = ["j", "yy", "hh"]
list_a.extend(list_b)
print(list_a)


# adding an item to a list using the insert() method
list_a.insert(0, "Chinedu")
print(list_a)


# Changing the content of a list using the = operator
list_a[4] = "j"
print(list_a[4])


# Removing an item from a list using the del() method
del list_a[0]
print(list_a)


# Removing an item from a list using the remove() method
list_a.remove("yy")
print(list_a)


# Removing an item from a list using the pop() method
list_a.pop(3)
print(list_a)


# clearing all the items in a list
# list_a.clear()
# print(list_a)




# finding the position of an element in a list
print(list_a.index("hh"))



# Finding the count of elements in a list
print(list_a.count("hh"))


#sorting the list using the sort() method
list_c = [1, 3, 4, 65, 656, 7676,]
list_c.sort()
print(list_c)
list_c.sort(reverse=True)
print(list_c)


# Reversing the items of the list
list_c.reverse()
print(list_c)


# Creating a shallow copy of the list using the copy() method
list_d  =  list_a.copy()
print(list_d)



# iterating through a list using the for loop
languages = ['Python', 'Swift', 'C++']
for language in languages:
    print(language)



# List comprehension
numbers = [number*number for number in range(1, 6)]
print(numbers)


