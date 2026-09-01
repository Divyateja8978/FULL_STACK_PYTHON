#using for loop
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    print("Number:", num)
    total = total + num
print("Total:", total)
#using while loop
i = 1
total = 0

while i <= 5:
    print("Number:", i)
    total = total + i
    i = i + 1

print("Total:", total)

#Multiplication program
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
#factorial
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i

print("Factorial:", fact)