class product:
    isValid = True

    def __init__(self, price, name):
        self.price = price
        self.name = name

    @staticmethod
    def discount(x, y):
        return x + y


x = product(100, 'book')
print(x.discount(2, 3))

print(product.discount(2, 3))
