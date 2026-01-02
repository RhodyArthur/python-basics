#  Task 8.1: Palindrome checker (3 points)
# Write a function `is_palindrome(s)` that checks if a string is a palindrome. Ignore case and spaces.

def is_palindrome(s):
    cleaned_str = "".join(s.split()).lower()
    reversed_str = cleaned_str[::-1]
    if reversed_str == cleaned_str:
        return True
    return False

# Task 8.2: Count vowels (3 points)
# Write a function `count_vowels(s)` that counts the number of vowels in a string.

def count_vowels(s):
    vowels = ['a','e','i','o','u']
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count

# Task 8.3: Capitalize words (3 points)
# Write a function `capitalize_words(sentence)` that capitalizes the first letter of each word **WITHOUT** using `.title()`.

def capitalize_words(sentence):
    return ' '.join([word[0].upper()+word[1::] for word in sentence.split()])

print(capitalize_words("A man a plan a canal Panama"))
