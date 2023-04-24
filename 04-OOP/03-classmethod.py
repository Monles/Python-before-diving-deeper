class product:
    isValid = True

    def __init__(self, price, name):
        self.price = price
        self.name = name

    def discount(self):
        print(f'Now {self.name} is on sale. Only $20.')

    @classmethod
    def more_discount(cls, a, b):
        return a + b


a = product(100, 'book')
print(a.more_discount(2, 3))
