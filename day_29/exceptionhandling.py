#syntax error
if 10 > 5
    print("10 is greater")
#runtime error
a = 10
b = 0

print(a / b)
#logical error
a = 10
b = 20

result = a - b

print("Addition:", result)
#try &except
try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")
#try-except-else
try:
    a = 10
    b = 2
    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)
#finally
try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program completed")