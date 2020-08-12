from veho.matrix.margin import margin_mutate

mx = [[i + j for j in range(6)] for i in range(8)]

print('original')
print(mx)

print(margin_mutate(mx, lambda x: f'({x})', 3, 2, 2, 1))
