

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