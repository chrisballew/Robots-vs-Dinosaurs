from Weapons import Weapon

class Robot:
    def __init__(self, name): #possibly add power level later
        self.robo_name = name
        self.robo_health = 500
        self.weapon = Weapon #weapon will need user input to select weapon
    
    #three different robot objects needed?
    
    def robot_attack(self, dinosaur):
        pass