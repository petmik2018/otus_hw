from src.figure import Figure


class Rectangle(Figure):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def calc_perimeter(self):
        return 2 * (self.width + self.height)

    def calc_area(self):
        return self.width * self.height
