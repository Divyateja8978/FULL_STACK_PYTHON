#sets
student_ids = {101, 102, 103, 104}
print(student_ids)

#datatype
student_ids = {101,102,103,104}
print(type(student_ids))

#Adding element 
fruits = {"Apple","Mango"}
fruits.add("Orange")
print(fruits)

#dictionary
student = {
    "name":"Raju",
    "age":21,
    "city":"Hyd"
}
print(student["name"])
print(student["city"])

#Boolean
print(10 == 10)
print(10 > 5)

#implicit type casting
a = 10        # int
b = 12.5      # float
print(a + b)

#Excplict type casting
a = 10
print(a, type(a))
b = float(a)
print(b, type(b))
c = str(a)
print(c, type(c))
d = bool(a)
print(d, type(d))
a = 10.5
print(int(a))
numbers = [10,20,30]
print(tuple(numbers))
numbers = [10,20,20,30]
print(set(numbers))
name = "Python"
print(list(name))
name = "Python"
print(tuple(name))
name = "Python"
print(set(name))
data = [
    ("name", "Raju"),
    ("age", 23)
]
student = dict(data)
print(student)