from aryth.bound_vector.bound import bound
from resources import RT

paramsList = {
    'one_zero': [0],
    'one_nan': [None],
    'asc_6': [0, 1, 2, 3, 4, 5],
    'desc_6': [5, 4, 3, 2, 1, 0],
    'misc': [False, 101, 102, 103, 104],
    'misc2': [1, 2, None, 4, 5],
    'tx_nums': ['244', '200', '306', '400', '150', '220', '190', '495'],
    'tx_strs': 'comprehend how it\'s driven by animal spirits'.split(' '),
}


def test():
    for key, vec in paramsList.items():
        print(key, RT, bound(vec, True))


test()
