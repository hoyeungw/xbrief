def margin_shallow(vec, h, t):
    return vec[:h] + vec[-t:]


def margin_mapper(vec, fn, h, t):
    return [fn(x) for x in vec[:h]] + [fn(x) for x in vec[-t:]]


def margin_mutate(vec, fn, h, t):
    for i in range(h):
        vec[i] = fn(vec[i], i)
    size = len(vec)
    for k in range(t):
        i = size - k
        vec[i] = fn(vec[i], i)
    return vec
