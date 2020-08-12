import inspect
from math import sqrt


def props_by_vars(obj):
    # for property, value in vars(obj).items():
    #     print(property, ": ", value)
    return vars(obj)


def props_by_inspect(obj):
    return inspect.getmembers(obj)


class Point:
    id = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    @staticmethod
    def build(x, y):
        return Point(x, y)


point = Point(3, 4)
point.id = '223'
print(type(point))
print('props_by_vars', props_by_vars(point))
print('props_by_inspect', props_by_inspect(point))
