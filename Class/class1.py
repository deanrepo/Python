class Monster:

    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def __len__(self):
        return 5
    
    def __add__(self, number):
        return self.health + number
    
    def __str__(self):
        return f'The monster health: {self.health} and the monster energy: {self.energy}'

    # method
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        print(self.energy)

    def move(self, speed):
        print(f'The monster move {speed}')

monster = Monster(10, 20)
print(len(monster))
print(monster.__dict__)
print(vars(monster))
print(monster + 55)
print(str(monster))
print(monster)
