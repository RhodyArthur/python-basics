# Task 2.1: Number classification function
# Write a function `classify_number(num)` that takes a number and returns:
# - "Positive" if number > 0
# - "Negative" if number < 0
# - "Zero" if number == 0

def classify_number(num):
    if num == 0:
        return "Zero"
    elif num > 0:
        return "Positive"
    else:
        return "Negative"


# Task 2.2: Age category function
# Write a function `age_category(age)` that returns:
# - "Child" if age < 13
# - "Teenager" if 13 <= age < 20
# - "Adult" if 20 <= age < 65
# - "Senior" if age >= 65

# def age_category(age):
