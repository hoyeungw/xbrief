from aryth.bound_vector.duobound import duobound
from resources import RT

paramsList = {
    'one_zero': [0],
    'one_nan': [None],
    'asc_4': [0, 1, 2, 3],
    'desc_4': [3, 2, 1, 0],
    'misc': [False, 101, True, 103],
    'misc2': [1, 't', None, 4, 'f'],
    'tx_nums': ['244', 200, '306', '...', 'ant', 400, ],
    'tx_strs': 'comprehend how it\'s driven by animal spirits'.split(' '),
}


def test():
    for key, vec in paramsList.items():
        print(key, RT, duobound(vec))


test()
