# Nested If-Else statements in python
a = 10
b = 20
c = 30
# Using nested if-else to check multiple conditions
if a < b:
    # If a is less than b, check if a is also less than c
    if a < c:
        print("a is less than both b and c")
    else:
        print("a is less than b but greater than c")
else:
    print("a is not less than b")
    