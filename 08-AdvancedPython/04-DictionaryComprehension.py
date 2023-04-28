a = {'I': 1, 'II': 2}

a = {k: v**2 for k, v in a.items() if v % 2 == 0}

print(a)
