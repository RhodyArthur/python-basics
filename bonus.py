# Bonus 1: Fibonacci sequence (4 points)
# Write a function `fibonacci(n)` that generates the Fibonacci sequence up to n terms.

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    result = [0, 1]
    
    while len(result) < n:
        result.append(result[-1] + result[-2])
    return result

# Bonus 2: Prime number checker (3 points)
# Write a function `is_prime(num)` that checks if a number is prime.
def is_prime(num):
    if num <= 1: return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Bonus 3: Second largest number (3 points)
# Write a function `second_largest(numbers)` that finds the second largest number in a list.
def second_largest(numbers):
    return sorted(numbers, reverse=True)[1]
            


