def fact(n):
    if n == 1:
        return 1
    
    return n * fact(n-1) # Factorial
    # return n + fact(n-1) Sum of N Numbers

print(fact(5))