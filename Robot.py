from weapon import Weapon
#fix import

class Robot:
    def __init__(self, name):
        self.robo_name = name
        self.robo_health = 500
        self.weapon = Weapon("graviton beam", 40) #weapon will need user input to select weapon
    
    def robot_attack(self, dinosaur):
        pass