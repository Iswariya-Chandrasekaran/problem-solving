import random
from Enemy import *

class Ogre(Enemy):
    def __init__(self, health_points, damage_point):
        super().__init__(type_of_enemy="Ogre",
                         health_points=health_points,
                        damage_point=damage_point
                        )
    def talk(self):
        print("Im Slamming")
    
    def special_attack(self):
        # random.random() gives random floating number betn 0.0 - 1.0. eg: 0.123,0.9
        # if it is less than 0.50 it produces true else false
        did_spl_attack=random.random() < 0.20
        if did_spl_attack:
            self.health_points+=4
            print(f"My health points increased by 2HP , now I have {self.health_points}")
        else:
            print("Better luck next time")

        
    

