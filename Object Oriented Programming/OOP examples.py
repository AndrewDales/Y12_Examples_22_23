class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initialization method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Defined method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    # description method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # detailed representation of the instance (for a developer)
    def __repr__(self):
        return f"Dog('{self.name}', {self.age})"

    # quick representation of the instance (for a user)
    def __str__(self):
        return f"{self.name}, {self.age}"
