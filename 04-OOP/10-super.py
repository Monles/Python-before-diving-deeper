class Character:

    # Constructor
    def __init__(self, na, po):
        self.name = na
        self.power = po

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.power)


class a(Character):

    def __init__(self, name, po):
        self.name_ = name

    def Print(self):
        print("Emp class called")


b = a("Alice", 20)

# calling parent class function
b.name_, b.name
