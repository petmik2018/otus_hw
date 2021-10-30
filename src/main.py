from triangle import Triangle
from rectangle import Rectangle
from square import Square
from circle import Circle

triangle = Triangle(2, 2, 2)

print(triangle.perimeter)
print(triangle.area)

rectangle = Rectangle(3, 5)
square = Square(3)

print(rectangle + square)

circle = Circle(2)
print(circle.area)




