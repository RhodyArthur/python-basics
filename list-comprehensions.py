# Task 7.1: Squares (2 points)
# Create a list of squares of numbers from 1 to 10 using list comprehension.
sq_nums = [i ** 2 for i in range(1, 11)]

# Task 7.2: Even numbers (2 points)
# Create a list of even numbers from 1 to 20 using list comprehension.
even_nums = [num for num in range(1, 21) if num % 2 == 0]
print(even_nums)

# Task 7.3: Tuples of numbers and squares (3 points)
# Create a list of tuples `(number, square)` for numbers 1 to 5 using list comprehension.
tuple_nums = [(num, num**2) for num in range(1, 6)]

# Task 7.4: Flatten nested list (3 points)
# Write a function `flatten(nested_list)` that flattens a 2D list using list comprehension.
# Example: `[[1, 2], [3, 4], [5]]` → `[1, 2, 3, 4, 5]`
def flatten(nested_list):
    result = []
    for num in nested_list:
        for i in num:
            result.append(i)
    return result