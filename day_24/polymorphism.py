class Dog:
    def sound(self):
        print("Dog says: Bow Bow")


class Cat:
    def sound(self):
        print("Cat says: Meow")


d = Dog()
c = Cat()

d.sound()
c.sound()
#Duck Typing
class Dog:
    def sound(self):
        print("Bow Bow")


class Cat:
    def sound(self):
        print("Meow")


for animal in [Dog(), Cat()]:
    animal.sound()
#operator overloading
print(10 + 20)
print("Hello " + "Python")
#method overriding
class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        print("Bow Bow")


d = Dog()
d.sound()
#method overloading
class Calculator:
    def add(self, a, b=0, c=0):
        print(a + b + c)


c = Calculator()

c.add(10)
c.add(10, 20)
c.add(10, 20, 30)
