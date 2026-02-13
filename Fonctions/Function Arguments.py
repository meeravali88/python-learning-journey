# Function Arguments

def evenOdd(x):
    # first condition is x modulo 2 is equal to 0, then return "Even" else return "Odd"
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

# test the function with two numbers, one even and one odd  and print the results
print("This number is " + evenOdd(16))
print("This number is " + evenOdd(7))