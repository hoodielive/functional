def factorial(n):
    result = 1 

    for x in range(2, n):
        result *= x 
    return result

print(factorial(5))

# turn it to a recursive function 

def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)
print(factorial(4))


def fib(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(7))