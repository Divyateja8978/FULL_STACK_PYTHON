class Student:
    college = "ABC Engineering College"

    def __init__(self, name, roll_no, age, marks):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.__marks = marks

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

    # Calculate grade
    def grade(self):
        if self.__marks >= 90:
            return "A+"
        elif self.__marks >= 80:
            return "A"
        elif self.__marks >= 70:
            return "B"
        elif self.__marks >= 60:
            return "C"
        elif self.__marks >= 40:
            return "D"
        else:
            return "Fail"

    # Display student details
    def display(self):
        print("\n----- Student Details -----")
        print("College:", Student.college)
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Age:", self.age)
        print("Marks:", self.__marks)
        print("Grade:", self.grade())


class GraduateStudent(Student):

    def __init__(self, name, roll_no, age, marks, department):
        super().__init__(name, roll_no, age, marks)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


# Creating students

s1 = Student("Divya", 101, 21, 85)

s2 = GraduateStudent("Teja", 102, 22, 92, "Computer Science")


# Display students

s1.display()
s2.display()


# Updating marks

print("\n----- Updating Marks -----")

s1.set_marks(95)

print("Updated Marks:", s1.get_marks())
print("Updated Grade:", s1.grade())