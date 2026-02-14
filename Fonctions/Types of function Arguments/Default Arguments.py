# it is possible to provide default values for arguments. 
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
# If we call the function without argument, it uses the default value. 
myFun(10)
# If we provide an argument, it uses the provided value.