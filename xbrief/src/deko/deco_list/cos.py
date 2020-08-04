from typing import Callable, List

from palett.preset import Preset


def cos(
        arr: list,
        read: Callable = None,
        head: int = None,
        tail: int = None,
        presets: List[Preset] = None,
):
    if not isinstance(arr, list):
        return str(arr)
    size = len(arr)
    if not size:
        return str(arr)
    return size


listCollection = [
    None,
    [],
    [1, 1, 2, 3, 5, 8, 13, 21],
    ['foo', 'bar', 'zen']
]


def test():
    for candidate in listCollection:
        print(cos(candidate))


test()
