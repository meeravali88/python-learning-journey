# This function calculates the factorial of a number using recursion.
def factorial(n):
    # The base case is when n is 0, where the factorial is defined to be 1.
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
    # The function calls itself with a smaller value of n until it reaches the base case.
      
print(factorial(4))