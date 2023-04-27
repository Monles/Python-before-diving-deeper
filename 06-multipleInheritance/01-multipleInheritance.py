class Character():

    def __init__(self, account):
        self.account = account
        print('init complete')

    def sign_in(self):
        print('Logged in!')


class Wizard(Character):

    def __init__(self, name, magic_power):
        self.name = name
        self.magic_power = magic_power

    def attack(self):
        print(f'Attack with magic power {self.magic_power}')


class Warrior(Character):

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def check_HP(self):
        print(f'HP is {self.hp}.')

    def run(self):
        print(f'{self.name} is running pretty fast.')


class HybridOne(Wizard, Warrior):

    def __init__(self, name, power, hp):
        Wizard.__init__(self, name, power)
        Warrior.__init__(self, name, hp)


a = HybridOne('Alice', 50, 100)
print(a.check_HP())
