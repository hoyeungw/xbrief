import random
from datetime import date

from veho.matrix import init

from test.assets.classes import Point

basics = {
    'none': None,
    'bool': bool(random.randint(0, 1)),
    'string': 'shakes',
    'number': 128,
    'date': date.today(),
    'tuple': ('left', 'centre', 'right')
}

vectors = {
    'void_vec': [],
    'void_matrix': [[]],
    'nested_vec:': [[[[[[[[[]]]]]]]]],
    'simple_vec': [1, 2, 3, 'foo', 'bar', 'zen'],
    'alphabetical': init(4, 7, lambda x, y: chr(63 + (x * 7) + y)),
}

misc = {
    'lambda': lambda x: str(x)
}

objects = {
    'point': Point(3, 4, 'initial_point')
}

misc_candidates = {
    **basics,
    **vectors,
    **misc,
    **objects
}
