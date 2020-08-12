from veho.entries.margin import margin_mapper

entries = [(i, f'a-{i}') for i in range(8)]

print('original')
print(entries)
print('margined')
print(margin_mapper(entries, lambda x, i: f'[{x}]', lambda x, i: f'({x})', 3, 2))
