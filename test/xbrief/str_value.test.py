from resources import SP
from xbrief.texting.str_value import str_value

stringValueCandidates = [
    *['A' * (i + 1) for i in range(8)],
    *'comprehend how it\'s driven by animal spirits'.split(SP),
    'Warren',
    'WSJ',
    'GlobalTimes',
    'ZZZZ',
    'zzzz',
    'MetalGear 1',
    'MetalGear 2'
]

print(stringValueCandidates)


def test():
    for word in stringValueCandidates:
        print(word, str_value(word))


test()
