class Character():

    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.my_dict = {'fruit': 'Apple', 'is_Reading': False}

    def __getitem__(self, i):
        return self.my_dict[i]

    def __str__(self):
        return f"{self.name}"

    def __len__(self):
        return 3

    def __del__(self):
        print('deleted')


b = Character('Alice', 20)

print(b.__str__())
print(str(b))

print(b.__len__())
print(len(b))

print(b['fruit'])
del b
