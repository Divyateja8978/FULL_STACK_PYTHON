#class program
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s = Student("Divya", 21)

s.display()
#object
class Student:
    def display(self):
        print("Hello, I am a student")


s1 = Student()

s1.display()
#attributes
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Divya", 21)

print("Name:", s1.name)
print("Age:", s1.age)
#instance variable
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Divya", 21)
s2 = Student("Teja", 22)

print(s1.name)
print(s2.name)
#calss or static variable
class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name


s1 = Student("Divya")
s2 = Student("Teja")

print(s1.name, s1.college)
print(s2.name, s2.college)
#local variable
class Student:
    def display(self):
        marks = 90
        print("Marks:", marks)


s = Student()
s.display()