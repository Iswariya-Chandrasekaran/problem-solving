class Enemy:
    def __init__(self,type_of_enemy: str, health_points: int, damage_point: float):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.damage_point = damage_point


    def talk(self):
        print(f"Im talking Im  {self.__type_of_enemy}")
        # print(f"Im walking with {self.health_points} and without {self.damage_point}")
    
    def get_enemytype(self):
        return self.__type_of_enemy
    
    def attack(self):
        print(f"")
        
    def special_attack(self):
        print("Enemy has no special attack")

    
