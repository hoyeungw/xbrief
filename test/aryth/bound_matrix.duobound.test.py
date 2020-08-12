from aryth.bound_matrix.duobound import duobound
from resources import RT

paramsList = {
    'row': [[5, 7, 9, 10, 6]],
    'column': [[5], [7], [9], [10], [6]],
    'simple': [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    'tx_mx': [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']],
    'mixed': [['1', '2', 3], ['4', '...', '6'], ['7', '8', 'else']],
    'w_none': [[None, None, None], [4, None, 6], [7, 8, 9]],
    'empty': [],
    'empty2': [[]],
}


def test():
    for key, mx in paramsList.items():
        print(key, RT, duobound(mx))


test()
