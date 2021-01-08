'''
Битва двух армий. Армия света, против Армии тьмы!!!
'''
import random
from time import sleep as sleep
class Warrior:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def get_info(self):
        return  self.name, self.health, 'HP'

class Army_dark_side(Warrior):
    def __init__(self, name, health, damage, side):
        super().__init__(name, health, damage)
        self.side = side

class Army_light_side(Warrior):
    def __init__(self, name, health, damage, side):
        super().__init__(name, health, damage)
        self.side = side

def choce_batle(Army):
    random.shuffle(Army)
    return Army[0]

def battle(unit1, unit2):
    while unit1.health > 0 and unit2.health > 0:
        kick = random.randint(1, 2)
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
        print(unit1.name, 'Убит!,', unit2.name, 'Победил!')
        return unit1
    else:
        print(unit2.name, 'Убит!,', unit1.name, 'Победил!')
        return unit2

def reinforcement_update(battle_list, reinforcement_list):
    if set(reinforcement_list) & set(battle_list) == set(battle_list):
        reinforcement_list.clear()
    return reinforcement_list

Light_warriors_list = []
Dark_warriors_list = []
Reinforcement_list_sitt = []
Reinforcement_list_jadi = []

Dart_Waider = Army_dark_side('Waider', 120, 25, 'Dark')
Dart_Sidius = Army_dark_side('Sidius', 100, 25, 'Dark')
Dart_Mall = Army_dark_side('Mall', 100, 20, 'Dark')
Master_Ioda = Army_light_side('Ioda', 100, 25, 'Light')
R2D2 = Army_light_side('R2D2', 100, 25, 'Light')
Obi_Van = Army_light_side('Obi_Van', 150, 25, 'Light')
for i in Dart_Waider, Dart_Sidius, Master_Ioda, Obi_Van, R2D2, Dart_Mall:
    if i.side == 'Dark':
        Dark_warriors_list.append(i)
    else:
        Light_warriors_list.append(i)

print([i.get_info() for i in Light_warriors_list], 'ПРОТИВ', [i.get_info() for i in Dark_warriors_list])
while len(Dark_warriors_list) > 0 and len(Light_warriors_list) > 0:
    choce_dark = choce_batle(Dark_warriors_list)
    if len(Dark_warriors_list) == 1:
        choce_dark = Dark_warriors_list[0]
    else:
        while choce_dark in Reinforcement_list_sitt:
            choce_dark = choce_batle(Dark_warriors_list)

    choce_light = choce_batle(Light_warriors_list)
    if len(Light_warriors_list) == 1:
        choce_light = Light_warriors_list[0]
    else:
        while choce_light in Reinforcement_list_jadi:
            choce_light = choce_batle(Light_warriors_list)

    print(choce_dark.get_info(), 'fight us', choce_light.get_info())
    strike = battle(choce_dark, choce_light)
    if strike in Dark_warriors_list:
        Dark_warriors_list.remove(strike)
        if len(Dark_warriors_list) >= 1:
            Reinforcement_list_jadi.append(choce_light)
            print('Ещё в строю у ситтов:', [i.get_info() for i in Dark_warriors_list])
            Reinforcement_list_jadi = reinforcement_update(Light_warriors_list, Reinforcement_list_jadi)


    elif strike in Light_warriors_list:
        Light_warriors_list.remove(strike)
        if len(Light_warriors_list) >= 1:
            Reinforcement_list_sitt.append(choce_dark)
            print('Ещё в строю у джедаев:', [i.get_info() for i in Light_warriors_list])
            Reinforcement_list_sitt = reinforcement_update(Dark_warriors_list, Reinforcement_list_sitt)

if len(Dark_warriors_list) < 1:
    print('Джедаи победили!')
    print('Выжили:', [i.get_info() for i in Light_warriors_list])
else:
    print('Ситты победили!')
    print('Выжили:', [i.get_info() for i in Dark_warriors_list])