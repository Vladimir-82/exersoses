from random import random as ran

class Warrior:
    def __init__(self, name, health, demage, side):
        self.name = name
        self.health = health
        self.demage = demage
        self.side = side

    def get_info(self):
        return self.side, self.name, self.health

Dart_Waider = Warrior('Waider', 120, 12, 'Dark-side')
Dart_Sidius = Warrior('Sidius', 100, 15, 'Dark-side')
Master_Ioda = Warrior('Ioda', 100, 15, 'Light-side')
Obi_Van = Warrior('Obi_Van', 150, 15, 'Light-side')

while
