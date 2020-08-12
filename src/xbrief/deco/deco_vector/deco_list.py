from typing import Callable, List

from palett import Preset
from veho.vector.length import length


def deco_list(
        arr: list,
        read: Callable = None,
        head: int = None,
        tail: int = None,
        presets: List[Preset] = None,
):
    size = length(arr)
    if not size:
        return str(arr)
    return str(list)
