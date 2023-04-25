from abc import ABC, abstractmethod


class Fruit(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Apple(Fruit):

    # overriding abstract method
    def noofsides(self):
        print("Apple 🍎")


class Banana(Fruit):

    # overriding abstract method
    def noofsides(self):
        print("Banana🍌")


class Pineapple(Fruit):

    # overriding abstract method
    def noofsides(self):
        print("🍍")


class Avocado(Fruit):

    # overriding abstract method
    def noofsides(self):
        print("🥑")


# Driver code
R = Apple()
R.noofsides()

K = Banana()
K.noofsides()

R = Pineapple()
R.noofsides()

K = Avocado()
K.noofsides()
