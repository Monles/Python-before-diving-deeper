import functools

a = [1, 3, 5, 6, 2]

print("sum", end=" ")
print(functools.reduce(lambda a, b: a + b, a))

print("max", end=" ")
print(functools.reduce(lambda a, b: a if a > b else b, a))
