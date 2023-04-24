class person:

    # class Object attribute
    membership = True

    # Instance attribute
    def __init__(self, name, age):
        if (self.membership):
            self.name = name
            self.age = 18

    def greeting(self):
        print('Heyyyyyyea!')


# Driver Code
# Object Instantiation
a = person('Alice', 18)
print(a)
print(a.name)
print(a.age)
print(a.membership)
a.greeting()
