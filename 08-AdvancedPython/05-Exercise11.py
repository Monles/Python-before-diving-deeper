a = ['r', 'g', 'u', 'd', 's', 'x', 'r', 'f', 'e', 'r', 'x', 'd']

b = list(set([x for x in a if a.count(x) > 1]))
print(b)
