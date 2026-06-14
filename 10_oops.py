# Example 1
class Student:
    pass

# Example 2
class Student:
    name = "John"

s = Student()
print(s.name)

# Example 3
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Mike")
print(s1.name)

# Example 4
class Student:
    def display(self):
        print("Hello")

s2 = Student()
s2.display()

# Example 5
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

s3 = Student("David")
s3.show()