def myFun(*args, **kwargs):
    
    # *args allows us to pass a variable number of non-keyword arguments to the function.
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)
# **kwargs allows us to pass a variable number of keyword arguments to the function.
    print("\nKeyword Arguments (**kwargs):")
    # We can access the keyword arguments using the items() method of the dictionary.
    for key, value in kwargs.items():
        # We can print the key and value of the keyword arguments.
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='learning', mid='of', last='python')