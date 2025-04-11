from figures import Square, Circle, Triangle

class FigureService:
    def __init__(self):
        self.figures = {
            "square": Square(),
            "circle": Circle(),
            "triangle": Triangle()
        }

    def get_figure_colors(self):
        return {
            figure_type: figure.color
            for figure_type, figure in self.figures.items()
        }

    def set_figure_color(self, figure_type, color):
        if figure_type in self.figures:
            self.figures[figure_type].color = color
            return True
        return False

    def set_all_figure_colors(self, color):
        for figure in self.figures.values():
            figure.color = color
        return True