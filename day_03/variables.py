#using third variable
a = 10
b = 20
temp = a
a = b
b = temp
print("a =", a)
print("b =", b)
#without third variable
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print(a, b)
#swapping
a = 10
b = 20
a, b = b, a
print(a, b)
#variables
age = 22
name = "Harish"
percentage = 95.5
print(age)
print(name)
print(percentage)
