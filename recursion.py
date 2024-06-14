import os
os.system('clear')

# *In each function created throughout these exercises the body of the function must contain a **dosctring** 
# (a first line with a string explaining what the function does).*


# Task 1: Recursion with no return (no unwinding)
# Create a recursive function named `countdown` with a single integer input argument that prints a countdown starting from the given number.

def countdown(num):
    '''This function prints a countdown 
    starting from the given number'''
    if num == 0:
        print(num)
    else:
        print(num)
        countdown(num - 1)

print('Task 1:')
countdown(5)



# Task 2: Recursion with return and instructions after return (non tail-recursive)
# Create a recursive function named `factorial` that returns the factorial of a number 
# (the number multiplied by every integer lower than the number and greater than 0).

def factorial(n): # docstring comments look so ugly and unnapealing to me - holy moly
    '''This function returns            
    the factorial of a number'''
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print('\nTask 2:')
print(factorial(0))
print(factorial(1))
print(factorial(10))


# Task 3: Recursion with return and instructions after return (non tail-recursive)
# Create a function called `harmonic_sum` that requires an integer as an argument. The function will return the harmonic sum of the integer.
# The harmonic sum is the sum of reciprocals of the positive integers. The harmonical sum of 2 is: 1/1 + 1/2 = 1.5
# The harmonic sum of 4 is: 1/1 + 1/2 + 1/3 + 1/4 = 2.083333333333333

def harmonic_sum(n):
    '''This function returns the 
    harmonic sum of the integer'''
    if n == 1:
        return 1
    else:
        return 1/n + harmonic_sum(n - 1)

print('\nTask 3:')
print(harmonic_sum(7))
print(harmonic_sum(4))