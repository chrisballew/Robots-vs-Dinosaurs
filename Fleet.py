from Weapons import Weapon
from Robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        weapon_1 = Weapon("Lightning Claws", 15)
        weapon_2 = Weapon("Graviton Gun", 30)
        weapon_3 = Weapon("Antimatter Cannon", 50)

        robot_1 = Robot("Grav-Warrior", weapon_1)
        robot_2 = Robot("Hunter-Killer", weapon_2)
        robot_3 = Robot("Annihilator", weapon_3)
        
        self.robots.append(robot_1)
        self.robots.append(robot_2)
        self.robots.append(robot_3)