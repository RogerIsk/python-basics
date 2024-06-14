import os
os.system('clear')


# Task 1 - Create a function named `get_html_greeting` that returns a static greeting message (i.e. Hello world).
# Then create a decorator named `make_bold` that takes a function returning a string and wraps it with a `<strong>` HTML tag.
# Decorate `get_html_greeting` with it.

# Task 2 - Keep the previous code and create an additional function named `get_custom_html_greeting` that requires two arguments named `first` and `last`. 
# Decorate this function with the decorator `make_bold` and adapt it to work with both `get_html_greeting` and `get_custom_html_greeting` 
# (both with positional and keyword arguments).

# Task 3 - Keep the previous code and change the `get_custom_html_greeting` function so that the `<strong>` tag only wraps the full name of the person.
# You will have to create another function returning the full name of the person and move the `make_bold` decorator there. 
# Then call the `get_full_name` function from `get_custom_html_greeting`.
# Additionally, create two new decorators called `make_italics` and `make_paragraph` to wrap the whole greeting HTML string with an `<em>` and a `<p>` tags.

# Task 4 - Now remove all the decorators and keep everything else. Create a unique decorator named `wrap_with` that will let us wrap a string with any tag. 
# This tag will be indicated as a parameter of the decorator. I.e:

# Functions that wrap around other functions (Decorator functions) ======================================

def make_bold(func): 
    def wrapper(*args, **kwargs):
        return f'<strong>{func(*args, **kwargs)}</strong>'
    return wrapper

def make_italics(func): 
    def wrapper(*args, **kwargs):
        return f'<em>{func(*args, **kwargs)}</em>'
    return wrapper

def make_paragraph(func): 
    def wrapper(*args, **kwargs):
        return f'<p>{func(*args, **kwargs)}</p>'
    return wrapper

def wrap_with(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
        return wrapper
    return decorator

# Normal functions ======================================================================================

def get_html_greeting(): 
    return 'Hello, World!'

def get_custom_html_greeting(first='There', last=''): 
    return f'Hello, {get_full_name(first, last)}!'

def get_full_name(first='There', last=''):
    return f'{first} {last}'

# Printing stuff on screen ==============================================================================

number_of_tags = input('Number of tags you want to try: ')
for tag in range(int(number_of_tags)):
    print(wrap_with(input('Tag: ', ))(get_custom_html_greeting)())

list = [{1, 2, 3, 4, 5}, {'rgergeg'}]
print(list[0][2])