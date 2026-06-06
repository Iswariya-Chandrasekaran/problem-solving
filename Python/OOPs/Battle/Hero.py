from Weapon import *

class Hero():
    def __init__(self, health_points, damage_attack):
        self.health_points=health_points
        self.damage_point=damage_attack
        self.is_weapon_equip = False
        self.weapon: Weapon=None

    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equip:
            self.damage_point += self.weapon.increase_attack
            self.is_weapon_equip = True
    def attack(self):
        print(f"Hero attacks for {self.damage_point} attack damage")

        