# Task 4.1: List operations (4 points)
# Create a list of 5 fruits and perform these operations:
# 1. Add an item at the end
# 2. Insert an item at position 2
# 3. Remove an item by value
# 4. Remove an item by index
# 5. Print the final list

fruits = ['apple', 'banana', 'grapes', 'cherry', 'mango']
fruits.append('pear')
fruits[2] = 'coconut'
fruits.remove('mango')
fruits.pop(3)
print(fruits)

# Task 4.2: Find maximum (4 points)
# Write a function `find_max(numbers)` that finds the maximum value in a list **WITHOUT** using the built-in `max()` function.

def find_max(numbers):
    max_num = float("-inf")

    for i in range(len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]

    return max_num
