
def nameAge(name, age):
    # The order of the arguments is important in this case. 
    # If we change the order, it will give us wrong output.
    print("Hi, I am", name)
    print("My age is ", age)
# prints the correct order of age and name.
print("Case-1:")
nameAge("Suraj", 27)
# If we change the order of the arguments, it will give us wrong output.
print("\nCase-2:")
nameAge(27, "Suraj")