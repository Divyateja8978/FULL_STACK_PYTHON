#recursion
def count(n):
    if n == 0:
        return
    print(n)
    count(n - 1)

count(5)
#using factorial

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = 5
print("Factorial =", factorial(num))

#fibonaci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(7):
    print(fibonacci(i), end=" ")
    
# sum of natural numbers
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

num = 5
print("Sum =", sum_natural(num))