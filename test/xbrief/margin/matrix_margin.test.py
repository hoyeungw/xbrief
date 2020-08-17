from ject import oneself
from texting import COSP, ELLIP, LF, SP
from veho.matrix import init

from xbrief.margin.matrix_margin.matrix_margin import MatrixMargin

params = {
    'c0021': (0, 0, 2, 1),
    'c0121': (0, 1, 2, 1),
    'c1032': (1, 0, 3, 2),
    'c1132': (1, 1, 3, 2),
    'c3232': (3, 2, 3, 2),
    'c9921': (9, 9, 3, 2),
    'c3299': (3, 2, 9, 9),
}

candidates = {
    'blank': [[]],
    'simple': init(8, 6, lambda x, y: x + y)
}

LFSP = LF + SP


def deco_matrix(mx):
    return '[' + LFSP + LFSP.join(['[' + COSP.join(row) + ']' for row in mx]) + LF + ']'


for key, vector in candidates.items():
    for param_name, (tp, bt, lf, rt) in params.items():
        print(key, param_name, (tp, bt, lf, rt),
              deco_matrix(MatrixMargin
                          .build(vector, tp, bt, lf, rt)
                          .stringify(oneself)
                          .to_matrix(ELLIP))
              )
