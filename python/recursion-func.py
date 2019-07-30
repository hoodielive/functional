def factorial(n):
    result = 1 

    for x in range(2, n):
        result *= x 
    return result

print(factorial(5))
