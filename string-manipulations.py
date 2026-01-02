#  Task 8.1: Palindrome checker (3 points)
# Write a function `is_palindrome(s)` that checks if a string is a palindrome. Ignore case and spaces.

# Example: "A man a plan a canal Panama" should return True

def is_palindrome(s):
    cleaned_str = "".join(s.split()).lower()
    reversed_str = cleaned_str[::-1]
    if reversed_str == cleaned_str:
        return True
    return False
