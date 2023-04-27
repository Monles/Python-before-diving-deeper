def Sum(a, i, n, count):

    if n <= i:
        return count

    count += a[i]

    count = Sum(a, i + 1, n, count)

    return count


a = [1, 2, 3, 4, 5]
count = 0
n = len(a)
print(Sum(a, 0, n, count))
