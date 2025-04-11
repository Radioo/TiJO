class Figure:
    def __init__(self, color="#808080"):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value


class Square(Figure):
    pass


class Circle(Figure):
    pass


class Triangle(Figure):
    pass