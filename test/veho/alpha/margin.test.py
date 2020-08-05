from resources import ELLIP
from utils.margin import sizing

listCollection = [
    None,
    [],
    [1],
    [1, 2, 3],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
]


def test():
    h = 3
    t = 1
    for vec in listCollection:
        (head, tail) = sizing(vec, h, t)
        dash = bool(tail)
        print(
            (head, tail),
            vec[:head] if head else '',
            ELLIP if dash else '',
            vec[-tail:] if tail else '',
        ) if vec else print(vec)


test()
