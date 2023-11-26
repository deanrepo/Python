class Monster:
    def __init__(self, func):
        self.func = func


class Attacks:
    def bite(self):
        print('bite attack')

    def strike(self):
        print('strike attack')

    def slash(self):
        print('slash attack')
    
    def kick(self):
        print('kick attack')

am = Attacks()
m1 = Monster(func=am.bite)
m1.func()