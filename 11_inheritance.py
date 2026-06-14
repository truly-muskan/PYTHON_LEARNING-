# Example 1
class Animal:
    pass

class Dog(Animal):
    pass

# Example 2
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    pass

Dog().sound()

# Example 3
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

d = Dog()
d.eat()
d.bark()

# Example 4
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    pass

Child().show()

# Example 5
class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    pass

Car().start()