class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)


s = Student("Divya", 90)

s.display()
#accessing
class Bank:
    def __init__(self):
        self.__balance = 5000

    def show_balance(self):
        print("Balance:", self.__balance)


b = Bank()

b.show_balance()
#using getter and setter method
class Student:
    def __init__(self, marks):
        self.__marks = marks

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter
    def set_marks(self, marks):
        self.__marks = marks


s = Student(80)

print("Old Marks:", s.get_marks())

s.set_marks(90)

print("New Marks:", s.get_marks())