from functools import reduce

# init
pets = ['sisi', 'bibi', 'titi', 'carla']


def a(s):
    return s.upper()


print(list(map(a, pets)))

# Zip
b = ['a', 'b', 'c', 'd', 'e']
c = [5, 4, 3, 2, 1]
print(list(zip(b, c)))

# Filter
scores = [73, 20, 65, 19, 76, 100, 88]


def d(score):
    return score > 50


print(list(filter(d, scores)))


# reduce
def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (c + scores)))
