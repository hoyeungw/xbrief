from veho.vector import margin_mutate

vec = [i for i in range(8)]

margined = margin_mutate(vec, lambda x, i: f'({x})', 3, 2)
print(margined)
