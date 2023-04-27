from functools import reduce

a = [1, 3, 5]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, a, 0))
print(f"list {a}")
