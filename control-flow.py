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
    

# Task 2.3: FizzBuzz
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


# Task 2.4: Sum with while loop 
def sum_to_hundred():
    total = 0
    n = 1
    while n <= 100:
        total += n
        n+=1
    return total
