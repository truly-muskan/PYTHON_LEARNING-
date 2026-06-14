# Example 1
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

Dog().sound()
Cat().sound()

# Example 2
for animal in [Dog(), Cat()]:
    animal.sound()

# Example 3
class Bird:
    def sound(self):
        print("Chirp")

Bird().sound()

# Example 4
animals = [Dog(), Cat(), Bird()]
for animal in animals:
    animal.sound()

# Example 5
def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())