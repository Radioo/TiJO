from abc import ABC, abstractmethod


class IDrawable(ABC):
    @abstractmethod
    def draw(self):
        pass


class Square(IDrawable):
    def __init__(self, a):
        self.a = a

    def draw(self):
        for side in range(0, self.a):
            print(self.a * "o ")
        print()


class Triangle(IDrawable):
    def __init__(self, h):
        self.h = h

    def draw(self):
        for side in range(0, self.h):
            print(side * "o ")
        print()


class FigureDrawer:
    def draw(self, figure):
        figure.draw()


# Usage
a = 5
h = 5

square = Square(a)
triangle = Triangle(h)

drawer = FigureDrawer()
drawer.draw(square)
drawer.draw(triangle)