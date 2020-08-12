from math import sqrt


class Point:
    id = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def info(self):
        return f'({self.x},{self.y})'

    def distance(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    @staticmethod
    def build(x, y):
        return Point(x, y)
