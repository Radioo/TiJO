import unittest

from src.rover import LunarRover

class TestLunarRover(unittest.TestCase):
    def setUp(self):
        self.rover = LunarRover()

    def test_initial_position(self):
        self.assertEqual(self.rover.get_location(), (0, 0, 'N'))

    def test_move_forward(self):
        self.rover.move_forward(3)
        self.assertEqual(self.rover.get_location(), (0, 3, 'N'))

    def test_move_backward(self):
        self.rover.move_backward(2)
        self.assertEqual(self.rover.get_location(), (0, -2, 'N'))

    def test_rotation_left(self):
        self.rover.rotate_left()
        self.assertEqual(self.rover.get_location(), (0, 0, 'W'))

    def test_rotation_right(self):
        self.rover.rotate_right()
        self.assertEqual(self.rover.get_location(), (0, 0, 'E'))

    def test_full_rotation(self):
        for _ in range(4):
            self.rover.rotate_right()
        self.assertEqual(self.rover.get_location(), (0, 0, 'N'))


if __name__ == "__main__":
    unittest.main()