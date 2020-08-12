from veho.entries.margin import margin_mapper, margin_mutate
from xbrief.margin.vector_margin import VectorMargin


class EntriesMargin(VectorMargin):
    # def __init__(self):
    #     VectorMargin.__init__(self,)

    def map(self, kfn, vfn=None, mutate=False):
        boot, mapper = (self.reboot, margin_mutate) if mutate else (self.clone, margin_mapper)
        return boot(mapper(self.vec, kfn, vfn, self.head, self.tail))

    def stringify(self, kfn, vfn=None, mutate=False):
        kfn = (lambda x: str(kfn(x))) if kfn else str
        vfn = (lambda x: str(vfn(x))) if vfn else kfn
        return self.map(kfn, vfn, mutate)
