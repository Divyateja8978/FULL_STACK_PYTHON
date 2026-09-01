#Reverse a number
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse:", reverse)

#Sum of digits

num = int(input("Enter a number: "))

total = 0

while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Sum of digits:", total)

#palindrome

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")