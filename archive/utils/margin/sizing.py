from veho.vector import length


def sizing(vec, head, tail):
    if not (size := length(vec)): return 0, 0
    elif (not head and not tail) or (head >= size): return size, 0
    else: return head, tail
