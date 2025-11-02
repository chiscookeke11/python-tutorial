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