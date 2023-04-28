def one(func):
    def a(*args, **kwargs):
        print("x" * 15)
        func(*args, **kwargs)
        print("x" * 15)
    return a


def another(func):
    def a(*args, **kwargs):
        print("o" * 15)
        func(*args, **kwargs)
        print("o" * 15)
    return a


@one
@another
def print_it(msg):
    print(msg)


print_it("Heyyy")
