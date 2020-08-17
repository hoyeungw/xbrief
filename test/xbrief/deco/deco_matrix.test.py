from veho.matrix import init

from xbrief.deco.deco_matrix import deco_matrix

candidates = {
    'blank': [[]],
    'simple': init(8, 6, lambda x, y: x + y)
}


def test():
    for key, matrix in candidates.items():
        print(key, matrix)
        print(key, deco_matrix(matrix))


test()
