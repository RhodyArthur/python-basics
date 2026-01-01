# Task 3.1: Basic function
# Write a function `add(a, b)` that takes two numbers and returns their sum.
def add(a, b):
    return a + b

# Task 3.2: Function with default parameters
# Write a function `greet(name, message="Hello")` that returns a greeting string combining the message and name. Default message should be "Hello".
def greet(name, message="Hello"):
    return f"{message}, {name}"

# Task 3.3: Function returning multiple values
# Write a function `rectangle_metrics(length, width)` that calculates and returns both the area and perimeter of a rectangle.
def rectangle_metrics(length, width):
    area = length * width
    perimeter = (2 * length) + (2 * width)

    return f"Area and perimeter of rectangle respectively: {area, perimeter}"


# Task 3.4: Function using *args
# Write a function `sum_all(*args)` that returns the sum of any number of arguments passed to it.
def sum_all(*args):
    total = 0
    for i in range(len(args)):
        total += args[i]

    return total


# Task 3.5: Function using **kwargs
# Write a function `create_profile(**kwargs)` that creates and returns a user profile dictionary from keyword arguments.
def create_profile(**kwargs):
    return kwargs
    # {key: value for key, value in kwargs.items()}