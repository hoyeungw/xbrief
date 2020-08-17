from texting import COSP, LF

from xbrief.padder.pad_matrix import pad_matrix

candidates = {
    'cities': [
        ['1', 'paris', '++++'],
        ['1.1', 'san fransisco', '+'],
        ['1.2', 'tokyo', '+++'],
        ['1.3', 'delhi', '+'],
        ['1.4', 'vienna', '++'],
    ]
}


def test():
    for key, vec in candidates.items():
        print(key)
        padded = pad_matrix(vec)
        print(LF.join(['[' + COSP.join(row) + ']' for row in padded]))


test()
