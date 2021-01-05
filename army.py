from random import randint as ran

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

print(Dark_warriors_list)
print(Light_warriors_list)
print(Neitral_warriors_list)

while len(Dark_warriors_list)>0 and len(Light_warriors_list)>0:
     choce_dark = choce_batle(Dark_warriors_list)
     choce_light = choce_batle(Light_warriors_list)
     print(choce_dark)
     #print(Dark_warriors_list[choce_dark], 'fight us', Light_warriors_list[choce_light])