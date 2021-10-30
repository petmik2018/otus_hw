# import sys
# sys.path.append('../')

from src.figure import Figure
import math


class Triangle(Figure):

    def __init__(self, side_1, side_2, side_3):
        super().__init__()
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        if self.side_1 > self.side_2 + self.side_3:
            raise ValueError
        if self.side_2 > self.side_1 + self.side_3:
            raise ValueError
        if self.side_3 > self.side_2 + self.side_1:
            raise ValueError

    def calc_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def calc_area(self):
        p2 = (self.side_1 + self.side_2 + self.side_3)/2
        return math.sqrt(p2 * (p2 - self.side_1) * (p2 - self.side_2) * (p2 - self.side_3))