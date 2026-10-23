
class Animal:
    def __init__(self, name):
        self.name = name 

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

# usage 

dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.speak())
print(cat.speak())
