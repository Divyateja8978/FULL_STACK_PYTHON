#instance method
class Student:
    def display(self):
        print("Hello Student")


s = Student()
s.display()
#class method
class Student:
    college = "ABC College"

    @classmethod
    def display(cls):
        print("College:", cls.college)


Student.display()
#static method

class Calculator:
    
    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))
#using self
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Divya", 21)

s1.display()
#using constructors
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Divya", 21)

s1.display()