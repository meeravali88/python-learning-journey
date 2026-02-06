# Walrus operator in Python

# It was introduced in Python 3.8.
# Example of using walrus operator
numbers = [1, 2, 3, 4, 5]
# The walrus operator (:=) allows you to assign and return a value in the same expression.
if (n := len(numbers)) > 3:
    print(f"List has {n} elements")