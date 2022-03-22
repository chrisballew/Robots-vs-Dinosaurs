from Dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()
       
    
    def create_herd(self):
        dino_1 = Dinosaur("Raptor", 15)
        dino_2 = Dinosaur("T-Rex", 30)
        dino_3 = Dinosaur("Megasaurus", 50)
        
        self.dinosaurs.append(dino_1)
        self.dinosaurs.append(dino_2)
        self.dinosaurs.append(dino_3)