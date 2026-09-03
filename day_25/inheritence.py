#inheritance
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


d = Dog()

d.eat()
d.bark()
#single inheritance
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


d = Dog()
d.eat()
d.bark()
#multiple inheritance
class Father:
    def house(self):
        print("Father's house")


class Mother:
    def car(self):
        print("Mother's car")


class Child(Father, Mother):
    pass


c = Child()

c.house()
c.car()
#multilevel inheritance
class Grandfather:
    def land(self):
        print("Grandfather's land")


class Father(Grandfather):
    def house(self):
        print("Father's house")


class Son(Father):
    def bike(self):
        print("Son's bike")


s = Son()

s.land()
s.house()
s.bike()
#hierarchical inheritance
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    def bark(self):
        print("Barking")


class Cat(Animal):
    def meow(self):
        print("Meowing")


d = Dog()
c = Cat()

d.eat()
d.bark()

c.eat()
c.meow()
#hybrid inheritance
class A:
    def show_a(self):
        print("Class A")


class B(A):
    def show_b(self):
        print("Class B")


class C(A):
    def show_c(self):
        print("Class C")


class D(B, C):
    def show_d(self):
        print("Class D")


d = D()

d.show_a()
d.show_b()
d.show_c()
d.show_d()