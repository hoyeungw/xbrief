pairCollection = [
    ([1, ], [3, ]),
    (None, [3, 4]),
    ([1, 2], None),
    ([1, 2], [3, 4]),
]


def test():
    for i, (alpha, beta) in enumerate(pairCollection):
        print(i, alpha + beta if alpha and beta else alpha if alpha else beta if beta else None)


test()
