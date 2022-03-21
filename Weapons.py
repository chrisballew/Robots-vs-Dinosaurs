class Weapon:
    def __init__(self, name, attack_power):
        self.weapon_name = name
        self.attack_power = attack_power
        

weapon_1 = Weapon("graviton beam", 40)
print(weapon_1.weapon_name)

weapon_2 = Weapon("lightning claws", 30)
print(weapon_2.weapon_name)

weapon_3 = Weapon("antimatter missiles", 50)
print(weapon_3.weapon_name)