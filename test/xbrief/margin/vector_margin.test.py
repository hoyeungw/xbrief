from ject import oneself
from texting import ELLIP

from xbrief.margin.vector_margin import VectorMargin

params = {
    'h0t0': (0, 0),
    'h0t1': (0, 1),
    'h1t0': (1, 0),
    'h1t1': (1, 1),
    'h3t2': (3, 2),
    'h10t10': (10, 10),
}

candidates = {
    'simple': [1, 2, 3, 4, 5, 6, 7, 8]
}

for key, vector in candidates.items():
    for param_name, (head, tail) in params.items():
        print(key,
              VectorMargin
              .build(vector, head, tail)
              .stringify(oneself)
              .to_list(ELLIP)
              )
