import Robot
import Dinosaur
from Herd import Herd
from Fleet import Fleet



class Battlefield:
    def __init__(self, ):
        self.fleet = Fleet()
        self.herd = Herd()
     
    def run_game(self):
        pass
        
    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs!")

    def battle(self):
        pass
    
    def dino_turn(self):
        pass
    
    
    def robo_turn(self):
        pass
    
    
    def show_dino_options(self):
        pass
    
    
    
    def show_robo_options(self):
        pass
    
    
    def display_winners(self):
        if self.dinos_alive == False:
            print("Dinosaurs rendered null. Robot Empire = victorious.")
        elif self.robots_alive == False:
            print("The robots have been ripped to scrap! The dinosaurs win!")