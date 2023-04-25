class Cat:

    def __init__(self, n, w):
        self.name = n
        self.weight = w

    def walk(self):
        print(f"{self.name} is walking!")


class Alice:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def walk(self):
        print(f"{self.name} is walking!")


class Bob:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def walk(self):
        print(f"{self.name} is walking!")


a = Cat("Cat", 10)
b = Alice("Alice", 20)
c = Bob("Bob", 30)

for x in (a, b, c):
    x.walk()
