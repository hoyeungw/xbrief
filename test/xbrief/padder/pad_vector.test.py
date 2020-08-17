from texting import LF

from xbrief.padder.pad_vector import pad_vector

candidates = {
    'cities': ['paris', 'london', 'tokyo', 'delhi', 'vienna']
}


def test():
    for key, vec in candidates.items():
        print(key)
        padded = pad_vector(vec)
        print(LF.join(['\'' + word + '\'' for word in padded]))


test()
