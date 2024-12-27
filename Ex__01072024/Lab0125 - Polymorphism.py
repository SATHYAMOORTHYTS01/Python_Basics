# Polymorphism
# Polymorphism is a concept in object-oriented programming
# that allows objects of different classes to be treated as objects of a common superclass.
# It is a way to perform a single action in different ways.

# Method overriding


class Shape:
    def area(self):
        print("Area of the shape")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return 3.14 * self.length * self.width
class Circle(Shape):
       # pass is a placeholder for future code

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
       # pass is a placeholder for future code

shape1 = Rectangle(5, 3)
print(shape1.area())  # Output: Area of the shape

shape2 = Circle(7)
print(shape2.area())  # Output: Area of the shape

shape3 = Shape()
shape3.area()
print(shape3.area())