# Keyword arguments are the arguments which are passed to a function with a keyword.

def student(fname, lname):
    # The order of the arguments does not matter when we use keyword arguments.
    print(fname, lname)
    
# We can call the function with keyword arguments.
student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')

# output will be same for both the function calls.
# becuase we are using keyword arguments, the order of the arguments does not matter.