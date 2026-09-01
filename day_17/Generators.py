#list compherenatin
numbers = [1, 2, 3, 4, 5]

even = [x for x in numbers if x % 2 == 0]

print(even)

#list using list compherhention

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print("Original List:", numbers)
print("Square List:", squares)

#using dictionary
students = {
    "Rahul": 85,
    "Priya": 72,
    "Arun": 90,
    "Divya": 65,
    "Kiran": 78
}

# Select students who scored 75 or more
passed_students = {
    name: marks
    for name, marks in students.items()
    if marks >= 75
}

print("All Students:", students)
print("Passed Students:", passed_students)

#using nested list
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [num for row in numbers for num in row]

print("Nested List:", numbers)
print("Single List:", result)

#Generators 
def count():
    for i in range(1, 6):
        yield i
g = count()
print(next(g))
print(next(g))
print(next(g))

#Generator for Processing Orders
def orders():
    order_list = ["Order 101", "Order 102", "Order 103", "Order 104"]

    for order in order_list:
        yield order


for order in orders():
    print("Processing:", order)