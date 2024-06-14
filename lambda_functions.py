import os
os.system('clear')



# Task 1 - Create a lambda function that adds 15 to a given number passed in as an argument. Assign the lambda function to a variable name called `add15`.

print('Task 1')
add15 = lambda x: x + 15
print(add15(1))
print(add15(-2))



# Task 2 - Define the functions `isOdd`, `isEven` and `getParity` from previous exercises, but now as lambda functions assigned to variables.

isOdd = lambda n: n % 2 != 0
isEven = lambda n: n % 2 == 0
getParity = lambda n, parity: isOdd(n) if parity == 'odd' else isEven(n)
print('\nTask 2')
print(isOdd(2), isEven(2))
print(isOdd(1), isEven(1))
print(getParity(2, 'odd'), getParity(2, 'even'))
print(getParity(1, 'odd'), getParity(1, 'even'))



# Task 3 - Define a lambda function assigned to a variable named `starts_with_p` that takes a single argument as a string. 
# Returns True if this string starts with P (case insensitive) and False if it does not.

print('\nTask 3')
starts_with_p = lambda s: s.lower().startswith('p')
print(starts_with_p("Python"))
print(starts_with_p("JavaScript"))
print(starts_with_p("pirate"))



# Task 4 - For a given list of numbers, use a lambda function to return the result of multiplying each number 
# by a given number stored in a variable named `factor` in the global scope.

print('\nTask 4')
numbers = [2, 4, 5, 7, 9, 14]
factor = 2
result = list(map(lambda x: x * factor, numbers))
print(result)