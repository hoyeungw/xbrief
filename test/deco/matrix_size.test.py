from veho.matrix.utils.size import size

candidates = {
    'none': None,
    'empty_vec': [],
    'empty_mat': [[]],
    'row': [[0, 1, 2]],
    'column': [[0], [10], [20]],
    'matrix': [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
}

for key, ob in candidates.items():
    print(key, size(ob))
