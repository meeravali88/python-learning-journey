# Match-Case Statement in Python
x = 10
# Using match-case statement to check the value of x
match x:
    case 10:
        print("x is 10")
    case 20:
        print("x is 20")
    case _:
        print("x is not 10 or 20")
        