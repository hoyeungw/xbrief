from Levenshtein._levenshtein import distance

countries = ['nigeria', 'india', 'nepal', 'pakistan', 'uzbekistan']
alphabets = ['d', 's', 'y', 'a', 'e']
numerics = [3, 1, 5, 7, 2]
# misc = []
# misc.extend(countries)
# misc.extend(numerics)
# vec = countries
# print(vec)
# vec.sort()
# print(vec)

some = alphabets[0]
for word in alphabets:
    print(some, word, distance(some, word))

vec = []
vec[1] = 1
vec[3] = 3
print(vec)


def duobound(words, filter_x, mapper_x, filter_y, mapper_y):
    ve_x = [], ve_y = []

    return ve_x, ve_y
