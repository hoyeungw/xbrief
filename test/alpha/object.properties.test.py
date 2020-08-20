import inspect

from test.assets.classes import Point
from xbrief import deco_dict
from xbrief.bracket import parenth
from xbrief.deco.deco_entries.deco_entries import deco_entries


def test():
    point = Point(x=3, y=4, id='ball')
    print('type:', (ty := type(point)).__name__, parenth(ty))
    print('is class instance:', inspect.isclass(type(point)))
    print('members:', deco_entries(inspect.getmembers(point)))
    print('property:', deco_dict(vars(point)))
    print('@property:', deco_entries(inspect.getmembers(type(point), predicate=lambda o: isinstance(o, property))))
    print('method:', deco_entries(inspect.getmembers(point, predicate=inspect.ismethod)))


test()
