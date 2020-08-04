from xbrief.util.curt import Curt
from dataclasses import dataclass


@dataclass
class Preci:
    head: int or None
    tail: int or None

    @staticmethod
    def from_arr(arr, head: int, tail: int):
        if arr:
            if head and 0 < head <= len(arr):
                if tail and 0 < tail <= len(arr):
                    h, t = arr[:head], arr[-tail:]
                else:
                    h, t = arr[:head], None
            else:
                if tail and 0 < tail <= len(arr):
                    h, t = None, arr[-tail:]
                else:
                    h, t = arr, None
        else:
            h, t = None, None
        return Preci(h, t)

    def to_list(self, element=None):
        if self.head:
            if self.tail:
                if element:
                    return self.head + [element] + self.tail
                else:
                    return self.head + self.tail
            else:
                return self.head
        else:
            if self.tail:
                if element:
                    return [element] + self.tail
                else:
                    return self.tail
            else:
                return []

    def ject_head(self, ject):
        if self.head and ject:
            self.head = ject(self.head)
        return self

    def ject_tail(self, ject):
        if self.tail and ject:
            self.tail = ject(self.tail)
        return self

    def map(self, abstract, abstract_tail=None):
        if self.head and abstract:
            head = [abstract(v) for v in self.head]
        else:
            head = self.head
        if self.tail:
            if abstract_tail is not None:
                tail = [abstract_tail(v) for v in self.tail]
            else:
                if abstract is not None:
                    tail = [abstract(v) for v in self.tail]
                else:
                    tail = self.tail
        else:
            tail = self.tail
        return Preci(head, tail)

    def stringify(self, fmt=None):
        if fmt:
            return self.map(lambda x: f'{x:{fmt}}')
        else:
            return self.map(lambda x: f'{x}')
