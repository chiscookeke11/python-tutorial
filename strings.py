greet = 'hello'
print(type(greet))


# accessing string characters in python
print(greet[1])



# accessing string characters through negative indexing
print(greet[-3])


# accessing strings characters by slicing
print(greet[2:4])



# NOTE: strings are immutable, however we can assign the variable name to a new string
message = 'Hello Amigos'
message = 'Hello friends'

print(message)



# We can create a multi-line string in python using the triple double-quotes
message = """
Never gonna give up

Never gonna let you down

"""
print(message)


# Python string operations
# 1. using the "==" to compare two strings to check if they are equal
# 2. Using  the "+" operator to join two strings; concatenation
# 3. We can iterate through a string using the "for" loop. e.g:

name = 'Chinedu'
for letter in name:
    print(letter)


# 4. We use the len() method to find the length of a string
print(len(greet))

#5. string membership test using the 'in' keyword
print('e' in greet)
print('el' not in greet)


# Python methods
# converting string to uppercase using the 'upper()' method
print(greet.upper())

# converting string to lowercase using the 'lower()' method
print(greet.lower())


# to return a tuple
print(greet.partition('e'))

# to replace a substring
print(greet.replace('e', 't'))



# finding a substring
print(greet.find('o'))


# removing trailing characters
university = 'University of Nigeria Nsukka   '
print(university.rstrip())



# using the split method to split strings from left
print(university.split('e'))


# checking if a string starts with the specified string
print(university.startswith('t'))


# checking for numeric characters
print(university.isnumeric())



print(university.index('U'))

# Note: Check out escape sequence that  will allow you use a double quote inside a string



#  the f-strings make it possible to print strinsg inside another string
print(f'{greet} my dear friend')

