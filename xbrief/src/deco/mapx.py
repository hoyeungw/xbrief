from xbrief.src.texting import pad_start, tag
from xbrief.resources import RN, AEU, ELLIP
from xbrief.util import Preci


def hbrief(lex: dict,
           delimiter=', ',
           read=None,
           head: int = None,
           tail: int = None):
    if read:
        abstract = lambda kv: f'{kv[0]}:({read(kv[1])})'
    else:
        abstract = lambda kv: f'{kv[0]}:({kv[1]})'
    preci = Preci \
        .from_arr(list(lex.items()), head, tail) \
        .map(abstract)
    elements = preci.to_list(ELLIP)
    if elements:
        return delimiter.join(elements)
    else:
        return AEU


def vbrief(lex: dict,
           read=None,
           head: int = None,
           tail: int = None):
    abstract = lambda kv: (f'{kv[0]}', f'{read(kv[1])}') if read \
        else lambda kv: (f'{kv[0]}', f'{kv[1]}')
    preci = Preci \
        .from_arr(list(lex.items()), head, tail) \
        .map(abstract)
    length = max(preci.map(lambda kv: len(kv[0])).to_list())
    # f'{kvp[0]: <{length}}', kvp[1]
    elements = preci \
        .map(lambda kvp: tag(pad_start(kvp[0], length), kvp[1])) \
        .to_list(pad_start(ELLIP, length))
    return RN.join(elements) if elements else AEU
