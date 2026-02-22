# This code calculates the nth Fibonacci number using a recursive approach.
def fibonacci(n):
    # Base cases: F(0) = 0, F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    # Recursive case: F(n) = F(n-1) + F(n-2)

print(fibonacci(10))
# The output will be 55, which is the 10th Fibonacci number.