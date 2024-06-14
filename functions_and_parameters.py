import os
import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()


# *In each function created throughout these exercises the body of the function must contain a **dosctring** 
# (a first line with a string explaining what the function does).*
# Task 1: Simple functions with single positional arguments
# Create tThen wo simple functions `isOdd` and `isEven` that each take a single Integer and return a Boolean indicating whether the passed value is odd or is even.
# *An integer is even if it can be divided by 2 to produce another integer value. It is odd when dividing it by two produces a decimal value.*
# use those functions with these test cases:

print('Task 1:')
num = 5

def isOdd(num: int) -> bool: 
    '''This function returns True if the number is odd, False otherwise.'''
    return num % 2 != 0

def isEven(num: int) -> bool:
    '''This function returns True if the number is even, False otherwise.'''
    return num % 2 == 0

print(isOdd(1), isEven(1))
print(isOdd(657842), isEven(657842))
print(isOdd(0), isEven(0))



# Task 2: Multiple positional arguments of different types
# Create a single function `getParity` that does the same thing as the two functions in the previous task. This new function will accept a new 
# positional argument of type String that will contain the type of parity we want to get (either `odd` or `even`).
# If thearity is differen argument pt than `odd` and `even` then it should output a string message `Parity indicated is unknown`.
# Then design your own test cases to replicate the ones in the previous task but using the new function. Add also the following test case at the end:

print('\nTask 2:')
num = 6.5
parity = 'odd'
def getParity(num: int, parity: str) -> bool:
    '''This function returns True if the number is even, False otherwise.'''
    if parity == 'odd':
        return num % 2 != 0    
    elif parity == 'even':
        return num % 2 == 0
    else:
        return 'Parity indicated is unknown'

print(getParity(5, parity), getParity(5, parity))
print(getParity(11, parity), getParity(11, parity))
print(getParity(65742, parity), getParity(65742, parity))
print(getParity(num, 'add'), getParity(num, 'number'))



# Task 3: Multiple keyword arguments of different types
# Create a single function `greet` that greets a person differently depending on the time of the day.
# To do that, you will need to define two parameters on the header, one of type `String` and the other one of type `Date`. 
# You must define them as **keyword arguments** and name them `name` and `date`.
# If the time of the date is before 12:00PM the function will return "Good Morning, *name_of_the_person*!", 
# if not it will return "Good Afternoon, *name_of_the_person*!".
# You can extended it to say Good Night at another time, if you like*.

print('\nTask 3:')
def greet(name: str, date: datetime) -> str:
    '''This function greets a person depending on the time of the day.'''
    if date.hour < 12:
        return f'Good Morning, {name}!'
    else:
        return f'Good Afternoon, {name}!'
print(greet( name="John", date=datetime.datetime(2021, 5, 7, 11, 59, 59)))
print(greet(date=datetime.datetime(2021, 5, 7, 12, 0, 1),name="John"))



# Task 4: Packing and unpacking positional arguments
# Create a function `sumAll` that gets the sum of all values in different lists. 
# The function will accept any number of lists, each containing a variable amount of integers.
# The function should return the sum of all numbers in any of those lists and it must accept **any** number of parameters (use packing).

test1 = [[0, 2, 4, 5]]
test2 = [[0, 2, 4, 5],
         [6],
         [0, 2, 4, 5, 1, 4, 3, 2]]

print('\nTask 4:')
def sumAll(args) -> int:
    '''This function returns the sum of all values in different lists.'''
    return sum([sum(lst) for lst in args])
print(sumAll(test1))
print(sumAll(test2))



# Task 5: Positional and keyword arguments + default values
# Create a `pig_latin` function. This function will receive any amount of String objects. 
# For each word in those strings, it should transform the word according to these rules:
# - If the word starts with vowel, add `ay` at the end.
# - If not, move the first letter to the end and add `ay`
# Additionally, the function will accept a **keyword argument** `suffix` that will allow us to change the suffix `ay` into any other of our choice. 
# If we don't specify this argument, it should keep using `ay` (*default argument*).
# You will define another **keyword argument** `single` with a Boolean value to indicate the type of output we want.
# This output should be a list containing all the strings passed for translation (the positional arguments), 
# unless the `single` argument is set to `True`, in which case it should return a single String object.
# *Consider only a, e, i, o and u as vowels.*
# *Attention!! The input strings may have more than one word in them, so you will have to split them first and loop through all the words.*
# Call the function (using unpacking) with the following test cases:

print('\nTask 5:')
def pig_latin(words, suffix='ay', single=False):
    result = []
    for word in words: # 1 string at a time
        words_split = word.split()
        for word in words_split: # 1 word at a time
            if word[0].lower() in 'aeiou': 
                translated_word = word + suffix # new word = normal word + suffix
            else:
                translated_word = word[1:] + word[0] + suffix # move the first letter to the end and add suffix
            result.append(translated_word) # add the translated word to the result list
    if single:
        return ' '.join(result)
    else:
        return result

# Test cases
test1_data = ["Word", "Apple"]
test1_config = {}

test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}

test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}

print(pig_latin(test1_data))               
print(pig_latin(test1_data, single=True))
print(pig_latin(test2_data))               
print(pig_latin(test2_data, single=True))
print(pig_latin(test3_data))               
print(pig_latin(test3_data, single=True))