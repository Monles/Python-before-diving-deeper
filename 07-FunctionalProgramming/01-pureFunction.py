def pure_func(List):

    a = []

    for i in List:
        a.append(i * 2)

    return a


x = [1, 2, 3, 4]
y = pure_func(x)

print("Original ", x)
print("Modified ", y)
