from src.figure import Figure


class Square(Figure):

    def __init__(self, side):
        super().__init__()
        self.side = side

    def calc_perimeter(self):
        return 4 * self.side

    def calc_area(self):
        return self.side ** 2