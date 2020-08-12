from veho.matrix import iterate

mat = [
    [1, 2, 3],
    [1, 2, 3]
]


def fn(x, i, j): print(x, i, j)


iterate(mat, fn)
print(mat)
