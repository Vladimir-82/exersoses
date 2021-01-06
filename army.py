from random import randint as ran
from time import sleep as sleep
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

def choce_batle(Army):
    choice = ran(0, len(Army)-1)
    return choice

def battle(unit1, unit2):
    while unit1.health > 0 and unit2.health > 0:
        kick = ran(1, 2)
        if kick==1:
            print(unit1.name, 'наносит удар')
            sleep(1)
            unit2.health = unit2.health - unit1.damage
            print(unit2.get_info(), 'урон=', unit1.damage)
        elif kick == 2:
            print(unit2.name, 'наносит удар')
            sleep(1)
            unit1.health = unit1.health - unit2.damage
            print(unit1.get_info(), 'урон=', unit2.damage)
    if unit1.health <= 0:
        print(unit1.name, 'убит')
    else:
        print(unit2.name, 'убит')

    #print(unit1.name, 'убит' if unit1.health <= 0 else unit2.name, 'убит')

Light_warriors_list = []
Dark_warriors_list = []
Neitral_warriors_list = []


Dart_Waider = Army_dark_side('Waider', 120, 12, 'Dark')
Dark_warriors_list.append(Dart_Waider.name)
Dart_Sidius = Army_dark_side('Sidius', 100, 15, 'Dark')
Dark_warriors_list.append(Dart_Sidius.name)
Master_Ioda = Army_light_side('Ioda', 100, 15, 'Light')
Light_warriors_list.append(Master_Ioda.name)
Obi_Van = Army_light_side('Obi_Van', 150, 15, 'Light')
Light_warriors_list.append(Obi_Van.name)
Bobo_Fet = Neitral('Bobo', 50, 5, 'Neitral')
Neitral_warriors_list.append(Bobo_Fet.name)

battle(Dart_Waider, Obi_Van)

#while len(Dark_warriors_list) > 0 and len(Light_warriors_list) > 0:
     #choce_dark = choce_batle(Dark_warriors_list)
     #choce_light = choce_batle(Light_warriors_list)
     #print(Dark_warriors_list[choce_dark], 'fight us', Light_warriors_list[choce_light])

