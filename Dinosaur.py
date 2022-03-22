class Dinosaur:
    def __init__(self, name, attack_power):
        self.type = type
        self.attack = attack_power
        self.health = 500
       
    
    def dinosaur_attack(self, robot, attack_power):
        if self.health > 0:
            robot.health = robot.health - self.attack
            print(f'{robot.type} HP is now {robot.health}')