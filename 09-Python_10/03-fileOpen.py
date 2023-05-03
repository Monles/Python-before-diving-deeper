file1 = open("test.txt")


# read all
print(file1.read())
file1.seek(0)
print(file1.read())

# read the first line only
print(file1.readline())
