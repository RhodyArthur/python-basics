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
# print(fruits)

# Task 4.2: Find maximum (4 points)
# Write a function `find_max(numbers)` that finds the maximum value in a list **WITHOUT** using the built-in `max()` function.

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num


# Task 4.3: Reverse a list (4 points)
# Write a function `reverse_list(lst)` that reverses a list **WITHOUT** using `reverse()` or `[::-1]` slicing.
def reverse_list(lst):
    result = []

    if len(lst) == 0: return

    for i in range(len(lst)-1, -1, -1):
        result.append(lst[i])
    return result

# Task 4.4: Remove duplicates (4 points)
# Write a function `remove_duplicates(lst)` that removes duplicates from a list while keeping the original order.
def remove_duplicates(lst):
    result = []
    
    for el in lst:
        if el not in result:
            result.append(el)
    return result

# Task 4.5: Find common elements (4 points)
# Write a function `find_common(list1, list2)` that finds and returns common elements between two lists.

def find_common(list1, list2):
    common_elements = []
    for el in list1:
        if el in list2:
            common_elements.append(el)
    return common_elements
