class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
    def bark(self):
        print(self.name)

dog1 = Dog("Buddy", 3)
dog1.bark()