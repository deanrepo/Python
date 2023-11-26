class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def __str__(self):
        return f'The monster health: {self.health} and the monster energy: {self.energy}'

    # method
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of  {speed}')


class Shark(Monster):
    def __init__(self, speed, health, energy):
        super().__init__(health, energy)
        self.speed = speed

    def bite(self):
        print('The shark has bitten')

    def move(self):
        print('The shark has moved')
        print(f'The speed of the shark is {self.speed}')


class Scropion(Monster):
    def __init__(self, health, energy, poison_damage):
        super().__init__(health, energy)
        self.posion_damage = poison_damage

    def attack(self):
        print('The scropion has attacked!')
        print(f'{self.posion_damage} posion damage was dealt')
        self.energy -= 20

s = Scropion(100, 100, 20)
s.attack()
print(s.health)
print(s.energy)
    