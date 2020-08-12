from xbrief.texting.has_ansi import has_ansi
from xbrief.texting.lange import lange

candidates = [
    'tora',
    '\u001B[4mcake\u001B[0m',
    '\u001b[38;2;255;255;85mTolstoy\u001b[0m',
    # '\u{1F4A9}',
    '𝐀',
    'I \u2661 STEAK',
    '\u001b[3;4;31mhatsu\u001b[0m',
    # '\u{1F3C3}2\u{1F525}7',
    '\u001B[0m\u001B[4m\u001B[42m\u001B[31mfoo\u001B[39m\u001B[49m\u001B[24mfoo\u001B[0m🦄bar'
]

for tx in candidates:
    print(f'[{tx}] [has_ansi] ({has_ansi(tx)}) [lange] ({lange(tx)})')
