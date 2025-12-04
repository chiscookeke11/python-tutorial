

student_id = {112, 4555, "34", 5454, 65656}
print('student ID:', student_id)


# to create an empty set
empty_set = set()

# create an empty dicionary
empty_dict = {}



# testing duplicate items in a set
numbers = {2, 4, 6, 6, 2, 8,}
print(numbers)


# adding items to a set using the add() method
numbers.add(32)
print(numbers)

numbers.add(43)
print(numbers)

# updating a set using the update() method
companies = {'lacoste', 'berlin'}
tech_companies = ['Apple', 'Orange']
companies.update(tech_companies)
print(companies)



# removing an element from a set using the discard() method
languages = {'js', 'CSS', 'Swift'}
removedValue = languages.discard('Swift')
print(languages)



# using the all() method. This returns true if every element in the set is truthy
s = {1, 2, 4,}
print(all(s))

s2 = {1, 0, 3}
print(all(s2))




# using the any() method. This returns true if at least one is truthy.
s = {0, 0 , 5}
print(any(s))



s2 = {0, 0, 0}
print(any(s2))



# using the enumerate() method to return an enumerate object containing index + value pairs
s = {"a", "b", "c"}

for index, value in enumerate(s):
    print (index, value)





# using the len() method to get the length of the set
s = {10, 20, 30}
print(len(s))




# using the max() to get the largest number in the set
s = {4, 9, 5}
print("The largest number:", max(s))




# Using the min() to get the smallest number in a set
s = {4, 9, 3}
print(min(s))




# using the sorted() to sort elements in a set
print(sorted(s))




# using the sum() to return the sum of all the numbers in the set
print(sum(s))



# iterating over a set
fruits = {"Apple", "Pineapple", "Orange"}

for fruit in fruits:
    print(fruit)



# Python set operations
A = {1, 4, 2, 4, 5, 8, 0}
B = {3, 43, 54, 2, 10, 8}


# getting the union of the set
print("the union of the set:", A | B)
print("the union of the set:", A.union(B))



# Getting the intersection of the set
print("The Intersection of the set:", A & B)
print("The Intersection of the set:", A.intersection(B))



# Getting the difference between two sets
print("the difference of the set:", A - B)
print("the difference of the set:", A.difference(B))



# Getting the symmetric difference of the set
print("The symmetric difference of the set:", A ^ B)
print("The symmetric difference of the set:", A.symmetric_difference(B))




#checking if two sets are equal
print("Are the sets equal?", A == B)



# The clear() method removes all elements from the set
s = {1, 2, 4,}
s.clear()
print(s)




# using the copy() method
s = {1, 2, 3}
c = s.copy()
print(c)



a = {1, 2, 3}
b = {2, 3, 5}
a.difference_update(b)
print(a)








# --------------------------
# Python Set Methods Example
# --------------------------

# 1. add() → Adds an element to the set
s = {1, 2, 3}
s.add(4)
print("add():", s)   # {1, 2, 3, 4}


# 2. clear() → Removes all elements
s2 = {1, 2, 3}
s2.clear()
print("clear():", s2)   # set()


# 3. copy() → Returns a copy of the set
s3 = {1, 2, 3}
c = s3.copy()
print("copy():", c)     # {1, 2, 3}


# 4. difference() → Returns items in one set but not another
a = {1, 2, 3}
b = {2, 3, 4}
print("difference():", a.difference(b))   # {1}


# 5. difference_update() → Removes shared items from the original set
a2 = {1, 2, 3}
b2 = {2, 3, 5}
a2.difference_update(b2)
print("difference_update():", a2)   # {1}


# 6. discard() → Removes an element if it exists (no error if it doesn’t)
s4 = {1, 2, 3}
s4.discard(2)
print("discard(2):", s4)   # {1, 3}

s4.discard(10)             # No error
print("discard(10):", s4)  # {1, 3}


# 7. intersection() → Returns common elements as a new set
x = {1, 2, 3}
y = {2, 3, 4}
print("intersection():", x.intersection(y))   # {2, 3}


# 8. intersection_update() → Keeps only common elements (modifies original set)
x2 = {1, 2, 3}
y2 = {2, 3, 5}
x2.intersection_update(y2)
print("intersection_update():", x2)   # {2, 3}


# 9. isdisjoint() → True if sets have NO elements in common
d1 = {1, 2}
d2 = {3, 4}
print("isdisjoint():", d1.isdisjoint(d2))  # True

d3 = {2, 5}
print("isdisjoint():", d1.isdisjoint(d3))  # False


# 10. issubset() → True if this set is fully inside another set
sub1 = {1, 2}
sub2 = {1, 2, 3}
print("issubset():", sub1.issubset(sub2))  # True

sub3 = {1, 4}
print("issubset():", sub3.issubset(sub2))  # False



















