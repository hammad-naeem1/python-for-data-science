 #       (   oop    )
        # in Python is a programming paradigm that uses objects and classes
          #  to structure software into reusable, manageable pieces of code


class Dog:
    # The Constructor
    def __init__(self, name, breed):
        self.name = name    # Instance attribute
        self.breed = breed  # Instance attribute

    # Method (behavior)
    def bark(self):
        return f"{self.name} says Woof!"

# Creating objects (instances)
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Rex", "German Shepherd")

print(dog1.bark())  # Output: Buddy says Woof!
# ==============================

