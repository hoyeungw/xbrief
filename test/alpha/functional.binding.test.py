from types import MethodType


def deco_node_beta(self, node=None, level=0, indent=0):
    return str(self.level) + node


class Obj:
    pass


a = Obj()
a.level = 2

a.deco_node_beta = MethodType(deco_node_beta, a)
print(a.deco_node_beta('beta'))
