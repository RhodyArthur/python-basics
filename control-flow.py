# Task 2.1: Number classification function
def classify_number(num):
    if num == 0:
        return "Zero"
    elif num > 0:
        return "Positive"
    else:
        return "Negative"


# Task 2.2: Age category function
def age_category(age):
    if age <= 0:
        return "Age can't be less than or equal to 0"
    
    if age < 13:
        return "Child"
    elif (age >= 13 and age < 20):
        return "Teenager"
    elif (age >= 20 and age < 65):
        return "Adult"
    else:
        return "Senior"
    

# Task 2.3: FizzBuzz (4 points)
# Write a function `fizzbuzz(n)` that prints numbers 1 to n, but:
# - For multiples of 3, print "Fizz" instead of the number
# - For multiples of 5, print "Buzz" instead of the number
# - For multiples of both 3 and 5, print "FizzBuzz"

def fizzbuzz(n):
    for i in range(1, n+1):
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i)
