

def a(item):
    letters = ['ss', 'e', 'A', 'B', 'l']
    if (item in letters):
        return True
    else:
        return False


b = ['r', 't', 'E', 'b', 'kf', 'ss', 't', 'c', 'A']

x = filter(a, b)

print('The filtered letters are:')
for i in x:
    print(i)
