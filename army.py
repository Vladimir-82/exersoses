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

class Neitral(Warrior):
    def __init__(self, name, health, damage, side):
        super().__init__(name, health, damage)
        self.side = side


Dart_Waider = Army_dark_side('Waider', 120, 12, 'Dark')
Dart_Sidius = Army_dark_side('Sidius', 100, 15, 'Dark')
Master_Ioda = Army_light_side('Ioda', 100, 15, 'Light')
Obi_Van = Army_light_side('Obi_Van', 150, 15, 'Light')
Bobo_Fet = Neitral('Bobo', 50, 5, 'Neitral')

Light_warriors_list = []
Dark_warriors_list = []
Neitral_warriors_list = []
for j in Dart_Waider.name, Dart_Sidius.name, Master_Ioda.name, Obi_Van.name, Bobo_Fet.name:
    for i in Dart_Waider.side, Dart_Sidius.side, Master_Ioda.side, Obi_Van.side, Bobo_Fet.side:
        if i == 'Dark':
            Dark_warriors_list.append(j)
        elif i == 'Light':
            Light_warriors_list.append(j)
        else:
            Neitral_warriors_list.append(j)

print(Dark_warriors_list)
print(Light_warriors_list)
print(Neitral_warriors_list)