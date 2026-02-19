# in functions
def fun():
    pass

fun() # Call the function


# in if statement
x = 10

if x > 5:
    pass  # Placeholder for future logic
else:
    print("x is 5 or less")
    
  
# in loops  
for i in range(5):
    if i == 3:
        pass  # Do nothing when i is 3
    else:
        print(i)
        
        
# in classes   
class EmptyClass:
    pass  # No methods or attributes yet

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        pass  # Placeholder for greet method

# Creating an instance of the class
p = Person("Emily", 30)