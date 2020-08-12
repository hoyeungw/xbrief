from dataclasses import dataclass

from utils.margin.sizing import sizing
from veho.vector import margin_mapper, margin_mutate


@dataclass
class ListMargin:
    vec: list
    head: int
    tail: int

    @staticmethod
    def from_list(vec, head, tail):
        h, t = sizing(vec, head, tail)
        return ListMargin(vec, h, t)

    def map(self, func, mutate=False):
        if mutate:
            return self.reboot(margin_mutate(self.vec, func, self.head, self.tail))
        else:
            return self.clone(margin_mapper(self.vec, func, self.head, self.tail))

    def stringify(self, func=None, mutate=False):
        if func:
            return self.map(lambda x: str(func(x)), mutate)
        else:
            return self.map(str, mutate)

    def to_list(self, ellip=None):
        vec, head, tail = self.vec, self.head, self.tail
        if head:
            return ((vec[:head] + [ellip] + vec[-tail:])
                    if ellip
                    else (vec[:head] + vec[-tail:])) \
                if tail else vec[:head]
        else:
            return (([ellip] + vec[-tail:]) if ellip else vec[-tail:]) \
                if tail else []

    def reboot(self, vec):
        if vec:
            self.vec = vec
        return self

    def clone(self, vec):
        return ListMargin(vec, self.head, self.tail)
