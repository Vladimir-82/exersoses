from random import random as ran

class Warrior:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage


    def get_info(self):
        return  self.name, self.health

class Army_dark_side(Warrior):
    def __init__(self, name, health, damage, side):
        super().__init__(name, health, damage)
        self.side = side

class Army_light_side(Warrior):
    def __init__(self, name, health, damage, side):
        super().__init__(name, health, damage)
        self.side = side


Dart_Waider = Army_dark_side('Waider', 120, 12, 'Dark')
Dart_Sidius = Army_dark_side('Sidius', 100, 15, 'Dark')
Master_Ioda = Army_light_side('Ioda', 100, 15, 'Light')
Obi_Van = Army_light_side('Obi_Van', 150, 15, 'Light')
Bobo_Fet = Warrior('Bobo', 80, 7)

print(Master_Ioda.side)
print(Bobo_Fet.side)
