# Python Basics Assessment - Week 1-2 Topics

**Total Points: 110 (100 base + 10 bonus)**

**Time Limit: 2-3 hours**

**Instructions:**
- Complete all tasks in a Python file
- Test your code to ensure it works correctly
- Don't use external libraries - only built-in Python features
- Don't look up solutions - this assessment reveals your knowledge gaps

---

## SECTION 1: Variables, Data Types & Operators (10 points)

### Task 1.1: Create variables of different types (2 points)
Create variables for: an integer, float, string, boolean, and None type. Print each with its type using `type()`.

### Task 1.2: Perform arithmetic operations (2 points)
Calculate and store in variables:
- 47 + 23
- 100 - 37
- 12 * 8
- 144 / 12
- 17 // 5 (floor division)
- 17 % 5 (modulus)
- 2 ** 10 (exponentiation)

Print all results.

### Task 1.3: String operations (3 points)
Create two strings and demonstrate:
- Concatenation
- Repetition
- Getting the length

### Task 1.4: Type conversion (3 points)
Convert and print:
- "42" to int
- 3.14 to int
- 100 to string
- "True" to boolean (hint: what's the actual result?)

---

## SECTION 2: Control Flow (15 points)

### Task 2.1: Number classification function (3 points)
Write a function `classify_number(num)` that takes a number and returns:
- "Positive" if number > 0
- "Negative" if number < 0
- "Zero" if number == 0

```python
def classify_number(num):
    # Your code here
    pass
```

### Task 2.2: Age category function (4 points)
Write a function `age_category(age)` that returns:
- "Child" if age < 13
- "Teenager" if 13 <= age < 20
- "Adult" if 20 <= age < 65
- "Senior" if age >= 65

```python
def age_category(age):
    # Your code here
    pass
```

### Task 2.3: FizzBuzz (4 points)
Write a function `fizzbuzz(n)` that prints numbers 1 to n, but:
- For multiples of 3, print "Fizz" instead of the number
- For multiples of 5, print "Buzz" instead of the number
- For multiples of both 3 and 5, print "FizzBuzz"

```python
def fizzbuzz(n):
    # Your code here
    pass
```

### Task 2.4: Sum with while loop (4 points)
Write a function `sum_to_hundred()` that uses a while loop to calculate and return the sum of all numbers from 1 to 100.

```python
def sum_to_hundred():
    # Your code here
    pass
```

---

## SECTION 3: Functions (15 points)

### Task 3.1: Basic function (2 points)
Write a function `add(a, b)` that takes two numbers and returns their sum.

```python
def add(a, b):
    # Your code here
    pass
```

### Task 3.2: Function with default parameters (3 points)
Write a function `greet(name, message="Hello")` that returns a greeting string combining the message and name. Default message should be "Hello".

Example: `greet("Alice")` returns "Hello, Alice"

```python
def greet(name, message="Hello"):
    # Your code here
    pass
```

### Task 3.3: Function returning multiple values (3 points)
Write a function `rectangle_metrics(length, width)` that calculates and returns both the area and perimeter of a rectangle.

```python
def rectangle_metrics(length, width):
    # Your code here
    pass
```

### Task 3.4: Function using *args (4 points)
Write a function `sum_all(*args)` that returns the sum of any number of arguments passed to it.

Example: `sum_all(1, 2, 3, 4, 5)` returns 15

```python
def sum_all(*args):
    # Your code here
    pass
```

### Task 3.5: Function using **kwargs (3 points)
Write a function `create_profile(**kwargs)` that creates and returns a user profile dictionary from keyword arguments.

Example: `create_profile(name="John", age=30, city="NYC")` returns `{"name": "John", "age": 30, "city": "NYC"}`

```python
def create_profile(**kwargs):
    # Your code here
    pass
```

---

## SECTION 4: Lists (20 points)

### Task 4.1: List operations (4 points)
Create a list of 5 fruits and perform these operations:
1. Add an item at the end
2. Insert an item at position 2
3. Remove an item by value
4. Remove an item by index
5. Print the final list

### Task 4.2: Find maximum (4 points)
Write a function `find_max(numbers)` that finds the maximum value in a list **WITHOUT** using the built-in `max()` function.

```python
def find_max(numbers):
    # Your code here
    pass
```

### Task 4.3: Reverse a list (4 points)
Write a function `reverse_list(lst)` that reverses a list **WITHOUT** using `reverse()` or `[::-1]` slicing.

```python
def reverse_list(lst):
    # Your code here
    pass
```

### Task 4.4: Remove duplicates (4 points)
Write a function `remove_duplicates(lst)` that removes duplicates from a list while keeping the original order.

Example: `[1, 2, 2, 3, 4, 3, 5]` → `[1, 2, 3, 4, 5]`

```python
def remove_duplicates(lst):
    # Your code here
    pass
```

### Task 4.5: Find common elements (4 points)
Write a function `find_common(list1, list2)` that finds and returns common elements between two lists.

```python
def find_common(list1, list2):
    # Your code here
    pass
```

---

## SECTION 5: Dictionaries (15 points)

### Task 5.1: Create a student dictionary (3 points)
Create a dictionary representing a student with these keys:
- name (string)
- age (integer)
- grades (list of numbers)
- enrolled (boolean)

### Task 5.2: Word frequency counter (4 points)
Write a function `word_frequency(sentence)` that counts the frequency of each word in a sentence.

Example: `"hello world hello"` → `{"hello": 2, "world": 1}`

```python
def word_frequency(sentence):
    # Your code here
    pass
```

### Task 5.3: Merge dictionaries (4 points)
Write a function `merge_dicts(dict1, dict2)` that merges two dictionaries. If keys overlap, values from dict2 should overwrite dict1.

```python
def merge_dicts(dict1, dict2):
    # Your code here
    pass
```

### Task 5.4: Invert dictionary (4 points)
Write a function `invert_dict(d)` that inverts a dictionary (keys become values, values become keys). Assume all values are unique.

Example: `{"a": 1, "b": 2}` → `{1: "a", 2: "b"}`

```python
def invert_dict(d):
    # Your code here
    pass
```

---

## SECTION 6: Tuples & Sets (10 points)

### Task 6.1: Unpack tuple (3 points)
Create a tuple of coordinates `(x, y, z)`. Write a function `unpack_coordinates(coords)` that unpacks and returns them as three separate values.

```python
def unpack_coordinates(coords):
    # Your code here
    pass
```

### Task 6.2: Get unique elements (3 points)
Write a function `get_unique(lst)` that returns unique elements from a list using sets.

```python
def get_unique(lst):
    # Your code here
    pass
```

### Task 6.3: Set intersection (4 points)
Write a function `set_intersection(set1, set2)` that finds the intersection of two sets.

```python
def set_intersection(set1, set2):
    # Your code here
    pass
```

---

## SECTION 7: List Comprehensions (10 points)

### Task 7.1: Squares (2 points)
Create a list of squares of numbers from 1 to 10 using list comprehension.

### Task 7.2: Even numbers (2 points)
Create a list of even numbers from 1 to 20 using list comprehension.

### Task 7.3: Tuples of numbers and squares (3 points)
Create a list of tuples `(number, square)` for numbers 1 to 5 using list comprehension.

Example: `[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]`

### Task 7.4: Flatten nested list (3 points)
Write a function `flatten(nested_list)` that flattens a 2D list using list comprehension.

Example: `[[1, 2], [3, 4], [5]]` → `[1, 2, 3, 4, 5]`

```python
def flatten(nested_list):
    # Your code here
    pass
```

---

## SECTION 8: String Manipulation (15 points)

### Task 8.1: Palindrome checker (3 points)
Write a function `is_palindrome(s)` that checks if a string is a palindrome. Ignore case and spaces.

Example: "A man a plan a canal Panama" should return True

```python
def is_palindrome(s):
    # Your code here
    pass
```

### Task 8.2: Count vowels (3 points)
Write a function `count_vowels(s)` that counts the number of vowels in a string.

```python
def count_vowels(s):
    # Your code here
    pass
```

### Task 8.3: Capitalize words (3 points)
Write a function `capitalize_words(sentence)` that capitalizes the first letter of each word **WITHOUT** using `.title()`.

```python
def capitalize_words(sentence):
    # Your code here
    pass
```

### Task 8.4: Remove whitespace (3 points)
Write a function `remove_whitespace(s)` that removes all whitespace from a string.

```python
def remove_whitespace(s):
    # Your code here
    pass
```

### Task 8.5: Check if numeric (3 points)
Write a function `is_numeric(s)` that checks if a string contains only digits.

```python
def is_numeric(s):
    # Your code here
    pass
```

---

## BONUS CHALLENGES (10 extra points)

### Bonus 1: Fibonacci sequence (4 points)
Write a function `fibonacci(n)` that generates the Fibonacci sequence up to n terms.

Example: `fibonacci(7)` → `[0, 1, 1, 2, 3, 5, 8]`

```python
def fibonacci(n):
    # Your code here
    pass
```

### Bonus 2: Prime number checker (3 points)
Write a function `is_prime(num)` that checks if a number is prime.

```python
def is_prime(num):
    # Your code here
    pass
```

### Bonus 3: Second largest number (3 points)
Write a function `second_largest(numbers)` that finds the second largest number in a list.

```python
def second_largest(numbers):
    # Your code here
    pass
```

---

## Test Cases

Use these test cases to verify your solutions:

```python
if __name__ == "__main__":
    print("=== Testing Your Solutions ===\n")
    
    # Test Section 2
    print("Testing classify_number:")
    print(classify_number(5))  # Expected: "Positive"
    print(classify_number(-3))  # Expected: "Negative"
    print(classify_number(0))  # Expected: "Zero"
    
    print("\nTesting fizzbuzz(15):")
    fizzbuzz(15)
    # Expected: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
    
    # Test Section 3
    print("\nTesting add:")
    print(add(5, 3))  # Expected: 8
    
    print("\nTesting greet:")
    print(greet("Alice"))  # Expected: "Hello, Alice"
    print(greet("Bob", "Hi"))  # Expected: "Hi, Bob"
    
    # Test Section 4
    print("\nTesting find_max:")
    print(find_max([3, 7, 2, 9, 1]))  # Expected: 9
    
    print("\nTesting remove_duplicates:")
    print(remove_duplicates([1, 2, 2, 3, 4, 3, 5]))  # Expected: [1, 2, 3, 4, 5]
    
    # Test Section 5
    print("\nTesting word_frequency:")
    print(word_frequency("hello world hello"))  # Expected: {'hello': 2, 'world': 1}
    
    # Test Section 7
    print("\nTesting flatten:")
    print(flatten([[1, 2], [3, 4], [5]]))  # Expected: [1, 2, 3, 4, 5]
    
    # Test Section 8
    print("\nTesting is_palindrome:")
    print(is_palindrome("A man a plan a canal Panama"))  # Expected: True
    print(is_palindrome("hello"))  # Expected: False
    
    print("\nTesting count_vowels:")
    print(count_vowels("Hello World"))  # Expected: 3
    
    # Test Bonus
    print("\nTesting fibonacci:")
    print(fibonacci(7))  # Expected: [0, 1, 1, 2, 3, 5, 8]
    
    print("\nTesting is_prime:")
    print(is_prime(17))  # Expected: True
    print(is_prime(15))  # Expected: False
    
    print("\n=== Assessment Complete ===")
```

---

## Scoring Guide

- **90-110 points**: Excellent! You have a solid foundation in Python basics
- **70-89 points**: Good foundation, but review weaker areas before moving forward
- **50-69 points**: Some gaps exist, spend another week reinforcing fundamentals
- **Below 50 points**: Recommend revisiting Python basics more thoroughly

---

## Submission

When you're done:
1. Test all your functions with the provided test cases
2. Add additional test cases for edge cases (empty lists, None values, etc.)
3. Share your solution for review and feedback

Good luck! 🚀