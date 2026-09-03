#Arthemetic operators
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# assignment operators
a = 10
print("Assignment:", a)
a += 5
print("Addition assignment:", a)
a -= 3
print("Subtraction assignment:", a)
a *= 2
print("Multiplication assignment:", a)
a /= 4
print("Division assignment:", a)
a //= 2
print("Floor division assignment:", a)
a %= 3
print("Modulus assignment:", a)
a **= 2
print("Exponent assignment:", a)
a ^= 3
print("XOR assignment:", a)
a >>= 1
print("Right shift assignment:", a)
a <<= 2
print("Left shift assignment:", a)

#comparison operators
a = 10
b = 20
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)

#Logical operators
a = 10
b = 20
print("AND:", a < b and b > 15)
print("OR:", a > b or b > 15)
print("NOT:", not(a < b))

#bitwise operators
a = 10
b = 3
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

#membership operators
fruits = ["apple", "banana", "mango"]
print("apple in fruits:", "apple" in fruits)
print("grapes in fruits:", "grapes" in fruits)
print("apple not in fruits:", "apple" not in fruits)
print("grapes not in fruits:", "grapes" not in fruits)

#identity operators
a = [10, 20, 30]
b = a
c = [10, 20, 30]
print("a is b:", a is b)
print("a is c:", a is c)
print("a is not c:", a is not c)
print("a is not b:", a is not b)
