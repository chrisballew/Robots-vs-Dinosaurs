import Robot
import Dinosaur
from Herd import Herd
from Fleet import Fleet


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
     
    def run_game(self):
        self.display_welcome()
        self.battle() 
        self.display_winners()
    
    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs!")

    def battle(self):
        self.robots_alive = True
        self.dinos_alive = True
        while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:

            
            
            if len(self.fleet.robots) != 0:
                self.robo_turn()
                if self.herd.dinosaurs[0].health <= 0:
                    print(f'{self.herd.dinosaurs[0].type} has been exterminateds!')
                    self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
                
              
            
            
            if len(self.herd.dinosaurs) != 0:
                self.dino_turn()
                   
                if self.fleet.robots[0].health <= 0:
                    print(f'{self.fleet.robots[0].name} has been ripped to scrap!')
                    self.fleet.robots.remove(self.fleet.robots[0])
        
    
    
    def dino_turn(self):
        self.show_dino_opponent_options()
        self.herd.dinosaurs[0].dinosaur_attack(self.fleet.robots[0])
    
    
    def robo_turn(self):
        self.show_robo_opponent_options()
        self.fleet.robots[0].robot_attack(self.herd.dinosaurs[0])
    
    
    def show_dino_opponent_options(self):
        i = 1
        for robot in self.fleet.robots:
            print(f'{robot.name} has {robot.health} health')
            i += 1
    
    
    def show_robo_opponent_options(self):
         i = 1
         for dino in self.herd.dinosaurs:
            print(f'{dino.type} has {dino.health} health')
            i += 1
    
    
    def display_winners(self):
        if self.dinos_alive == False:
            print("The dinosaurs have been annihilated! The Robot Empire is victorious!")
        elif self.robots_alive == False:
            print("The robot invaders have been crushed! The dinosaurs win!")