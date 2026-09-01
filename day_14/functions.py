#Functions
def add(a, b):
    result = a + b
    print("Addition =", result)
add(10, 20)

#builtin methods
name = "divya teja"
numbers = [10, 20, 30, 40, 50]

# String built-in methods
print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("teja", "kumar"))

# List built-in methods
numbers.append(60)
numbers.insert(0, 5)
numbers.remove(30)
numbers.sort()

print(numbers)

# Built-in functions
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#userdefined 
def add(a, b):
    print("Addition =", a + b)

def subtract(a, b):
    print("Subtraction =", a - b)

def multiply(a, b):
    print("Multiplication =", a * b)

def divide(a, b):
    print("Division =", a / b)
add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 5)