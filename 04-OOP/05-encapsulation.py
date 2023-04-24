class product:

    def __init__(self, price, name):
        self.price = price
        self.name = name


x = product(120, 'book')
print(x.price)
print(x.name)

y = product(200, 'apple')
print(y.price)
print(y.name)
