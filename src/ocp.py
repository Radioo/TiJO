class Square:
    def __init__(self, a):
        self.a = a

    def draw(self):
        for side in range(0, self.a):
            print(self.a * "o ")
        print()

class Triangle:
    def draw_figure(self, h):
        for side in range(0, h):
            print(side * "o ")
        print()

class FigureDrawer:
    def draw_square(self, figure):
        figure.draw()

    def draw_triangle(self, figure, h):
        figure.draw_figure(h)

a = 5
h = 5

square = Square(a)
triangle = Triangle()

FigureDrawer().draw_square(square)
FigureDrawer().draw_triangle(triangle, h)