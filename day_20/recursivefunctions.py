#factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number: "))

result = factorial(num)

print("Factorial:", result)
#fibonaci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")
#sum ofnatural numbers
def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)


num = int(input("Enter a number: "))

result = sum_natural(num)

print("Sum:", result)

#pass by value
def change(x):
    x = 50
    print("Inside:", x)

a = 10

print("Before:", a)
change(a)
print("After:", a)
#pass by refeernce
def change_list(x):
    x.append(40)
    print("Inside function:", x)


numbers = [10, 20, 30]

print("Before:", numbers)

change_list(numbers)

print("After:", numbers)