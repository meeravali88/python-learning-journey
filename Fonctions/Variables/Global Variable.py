# Global Variables in Functions
msg = "Python is awesome!"
# This is a global variable defined outside any function

def display():
    # This function can access the global variable 'msg' and print its value
    print("Inside function:", msg)

display()
print("Outside function:", msg)
# The global variable 'msg' is accessible both inside and outside the function, demonstrating that it has a global scope.