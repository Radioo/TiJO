class LunarRover:
    def __init__(self, x=0, y=0, direction='N'):
        self.x = x
        self.y = y
        self.direction = direction

    def move_forward(self, steps=1):
        if self.direction == 'N':
            self.y += steps
        elif self.direction == 'E':
            self.x += steps
        elif self.direction == 'S':
            self.y -= steps
        elif self.direction == 'W':
            self.x -= steps

    def move_backward(self, steps=1):
        if self.direction == 'N':
            self.y -= steps
        elif self.direction == 'E':
            self.x -= steps
        elif self.direction == 'S':
            self.y += steps
        elif self.direction == 'W':
            self.x += steps

    def rotate_left(self):
        directions = ['N', 'W', 'S', 'E']
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def rotate_right(self):
        directions = ['N', 'E', 'S', 'W']
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def get_location(self):
        return self.x, self.y, self.direction