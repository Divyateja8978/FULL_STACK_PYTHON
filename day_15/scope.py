#Local scope
def display():
    x = 10
    print(x)

display()
#global scope
x = 10
def display():
  print(x)
display()
print(x)

# global keyword
x = 10
def change():
    global x
    x = 20
change()
print(x)
#Non local scope 
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)
outer()
#pass by value
def change(x):
    x = 20

a = 10
change(a)

print(a)
#pass by refernce
def change(numbers):
    numbers.append(40)
a = [10, 20, 30]
change(a)
print(a)

#pass by value and refernce
# Pass by value example
def change_value(x):
    x = 20
    print("Inside function:", x)

a = 10
change_value(a)
print("Outside function:", a)


# Pass by reference example
def change_list(numbers):
    numbers.append(40)
    print("Inside function:", numbers)

b = [10, 20, 30]
change_list(b)
print("Outside function:", b)
#Lambda function
multiply = lambda a, b: a * b
print(multiply(6, 5))
#Maximum
maximum = lambda a, b: a if a > b else b
print(maximum(10, 25))