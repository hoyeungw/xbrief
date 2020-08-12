from palett.fluo_vector import fluo_vector
from palett.presets import FRESH, PLANET
from resources import COSP

candidates = [
    [],
    ['Xx', 'Yy', 'Zz', 'e', 'd', 'c', '-', '1', 2, 3],
    [1, 1, 2, 3, 5, []],
    ['a', 'b', 'c', 'd', 'e'],
    ['beijing', 'shanghai', 'wuhan', 'xiamen', 'changsha']
]


def test():
    for vec in candidates:
        fluoed = fluo_vector(vec, (FRESH, PLANET))
        print(f'[{COSP.join(fluoed)}]')


test()