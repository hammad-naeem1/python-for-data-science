class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Controls how the object prints
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # Controls how the + operator behaves
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

# Usage
v1 = Vector(2, 4)
v2 = Vector(1, 3)

print(v1)        # Output: Vector(2, 4) (Thanks to __str__)
print(v1 + v2)   # Output: Vector(3, 7) (Thanks to __add__)

