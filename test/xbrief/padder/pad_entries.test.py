from texting import COSP, LF

from xbrief.padder.pad_entries import pad_entries

candidates = {
    'cities': [
        ('1', 'paris'),
        ('1.1', 'san fransisco'),
        ('1.2', 'tokyo'),
        ('1.3', 'delhi'),
        ('1.4', 'vienna'),
    ]
}


def test():
    for key, vec in candidates.items():
        print(key)
        padded = pad_entries(vec)
        print(LF.join(['(' + key + COSP + value + ')' for key, value in padded]))


test()
