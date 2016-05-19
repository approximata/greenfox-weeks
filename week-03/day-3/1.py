# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area

pi = 3.1415

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
            cf = 2 * self.radius * pi
            return cf

    def get_area(self):
            ae = self.radius ** 2 * pi
            return ae


c1 = Circle(4)

print(c1.get_circumference())
print(c1.get_area())
