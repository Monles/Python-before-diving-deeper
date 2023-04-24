class person:

    # class attribute
    membership = True

    # Instance attribute
    def __init__(self, name):
        self.name = name


Alice = person('Alice')
print(Alice)
print(Alice.name)
