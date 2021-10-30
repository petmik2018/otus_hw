from src.figure import Figure
import math


class Circle(Figure):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calc_perimeter(self):
        return 2 * math.pi * self.radius

    def calc_area(self):
        return math.pi * self.radius ** 2