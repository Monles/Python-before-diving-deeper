class Character(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isLoggedIn(self):
        return False


class Magician(Character):

    def isLoggedIn(self):
        return True


# Driver code
a = Character("Alice")
print(a.getName())
print(a.isLoggedIn())

b = Magician("Bob")
print(b.getName())
print(b.isLoggedIn())
