class Figure:

    def calc_area(self):
        return 0

    def calc_perimeter(self):
        return 0

    @property
    def area(self):
        return self.calc_area()

    @property
    def perimeter(self):
        return self.calc_perimeter()

    def __add__(self, other):
        if not isinstance(other, Figure):
            raise ValueError("Второй параметр не есть Фигура!!!")
        # return "Сумма площадей фигур: {}".format(self.calc_area() + other.calc_area())
        return self.calc_area() + other.calc_area()