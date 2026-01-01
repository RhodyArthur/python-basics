# Task 5.1: Create a student dictionary (3 points)
# Create a dictionary representing a student with these keys:
# - name (string)
# - age (integer)
# - grades (list of numbers)
# - enrolled (boolean)

student = {
    "name": "Esi Gyeyimah",
    "age": 24,
    "grades": [76, 89, 99],
    "enrolled": True
}

# Task 5.2: Word frequency counter (4 points)
# Write a function `word_frequency(sentence)` that counts the frequency of each word in a sentence.

def word_frequency(sentence):
    result = {}
    for word in sentence.split(' '):
        if word not in result:
            result[word] = 1
        else:
            result[word] = result[word] + 1
    return result