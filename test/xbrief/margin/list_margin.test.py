from archive.utils import ListMargin

listCollection = [
    None,
    [],
    [1],
    [1, 2, 3],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
]


def test():
    head, tail = (3, 2)
    for i, vec in enumerate(listCollection):
        margined = ListMargin.from_list(vec, head, tail).to_list('...')
        print(i, type(margined), margined)


test()
