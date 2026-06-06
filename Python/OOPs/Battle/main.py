from Enemy import *
from Zombie import *
from Ogre import *
from Hero import *

# def battle(e1: Enemy, e2: Enemy):
#     e1.talk()
#     e2.talk()
#     while e1.health_points>0 and e2.health_points>0:
#         print("------------------")
#         e1.special_attack()
#         e2.special_attack()
#         print(f"{e1.get_enemytype()} : {e1.health_points} hp left!")
#         print(f"{e2.get_enemytype()} : {e2.health_points} hp left!")
#         e2.attack()
#         e1.health_points -= e2.damage_point
#         e1.attack()
#         e2.health_points -= e1.damage_point
#     print("-----------------")
#     if e1.health_points> e2.health_points:
#         print(f"{e1.get_enemytype()} wins!!!")
#     else:
#         print(f"{e2.get_enemytype()} wins!!!")

def hero_battle(hero: Hero, enemy: Enemy):
    while hero.health_points>0 and enemy.health_points>0:
        print("------------------")
        enemy.special_attack()
        print(f" Hero : {hero.health_points} hp left!")
        print(f"{enemy.get_enemytype()} : {enemy.health_points} hp left!")
        enemy.attack()
        hero.health_points -= enemy.damage_point
        hero.attack()
        enemy.health_points -= hero.damage_point
    print("-----------------")
    if hero.health_points> enemy.health_points:
        print("Hero wins!!!")
    else:
        print(f"{enemy.get_enemytype()} wins!!!")


zombie=Zombie(10, 1)
ogre=Ogre(30, 3)
hero=Hero(10,1)
weapon=Weapon("Sword", 4)
hero.weapon=weapon
hero.equip_weapon()

hero_battle(hero,zombie)

# battle(zombie, ogre)
