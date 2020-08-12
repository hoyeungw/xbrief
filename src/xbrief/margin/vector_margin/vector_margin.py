from dataclasses import dataclass

from utils.margin.sizing import sizing
from veho.vector import margin_mapper, margin_mutate


@dataclass
class VectorMargin:
    vec: list
    head: int
    tail: int

    @staticmethod
    def from_list(vec, head, tail):
        h, t = sizing(vec, head, tail)
        return VectorMargin(vec, h, t)

    def map(self, func, mutate=False):
        boot, mapper = (self.reboot, margin_mutate) if mutate else (self.clone, margin_mapper)
        return boot(mapper(self.vec, func, self.head, self.tail))

    def stringify(self, func=None, mutate=False):
        fn = (lambda x: str(func(x))) if func else str
        return self.map(fn, mutate)

    def to_list(self, ellip=None):
        ve, h, t = self.vec, self.head, self.tail
        return (((ve[:h] + [ellip] + ve[-t:]) if ellip else (ve[:h] + ve[-t:]))
                if t
                else ve[:h]) if h else ((([ellip] + ve[-t:]) if ellip else ve[-t:])
                                        if t
                                        else [])

    def reboot(self, vec):
        if vec: self.vec = vec
        return self

    def clone(self, vec):
        return VectorMargin(vec, self.head, self.tail)
