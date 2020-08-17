from ject import oneself
from texting import ELLIP

from xbrief.margin.entries_margin import EntriesMargin

params = {
    'h0t0': (0, 0),
    'h0t1': (0, 1),
    'h1t0': (1, 0),
    'h1t1': (1, 1),
    'h3t2': (3, 2),
    'h10t10': (10, 10),
}

candidates = {
    'simple': [
        ('a', 1),
        ('b', 2),
        ('c', 3),
        ('d', 4),
        ('e', 5),
        ('f', 6),
        ('g', 7),
        ('h', 8),
        ('i', 9),
        ('j', 0),
    ]
}

for key, vector in candidates.items():
    for param_name, (head, tail) in params.items():
        print(
            key,
            EntriesMargin
                .build(vector, head, tail)
                .stringify(oneself)
                .to_list(ELLIP)
        )
