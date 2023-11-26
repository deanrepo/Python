class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def update_energy(self, amount):
        self.energy += amount

    def get_damage(self, amount):
        self.health -= amount


class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)
        

monster = Monster(100, 50)

hero = Hero(15, monster)

print(monster.health)
hero.attack()
print(monster.health)