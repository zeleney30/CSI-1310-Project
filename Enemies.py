from os import system, name
from os.path import exists
import os
import random
from re import A
import SkillPoints as Skills
import GameFunctions as Game
import Trader as Trader
import Dungeon as Dungeon
import Player as Player
import GameFunctions as Game

#current format: ["enemy name", health, damage] being 100% hit chance and 0% evasion chance
enemies = [["Grunt", 10, 2], ["Goblin", 15, 5], ["Zombie", 22, 9], ["Skeleton", 30, 12], ["Wizard", 42, 19]] #find a way to automatically increase difficulty based on level, skills, and armor
enemy = "Grunt" #only working enemy at this time -> makes it simpler for presentation purposes


dunOptions = {'1': 'Fight', '2': 'Use Consumable', '3': 'Flee'}
enemyhp = 10
enemydmg = 2

def GenerateEnemy():
    print("A " + enemy + " appeared!")
    print(dunOptions)

    key = input("Please select an option from the above list: ")
 
    if key == '1':
    #fight the enemy
        print("Fight!")
        enemyhp = 10
        while Player.hp > 0:
            Player.hp = Player.hp - enemydmg
            enemyhp = enemyhp - Player.dmg
            if enemyhp <= 0:
                print("You win!")
                Player.xp = Player.xp + 10
            elif Player.hp <= 0:
                print("You lose!")
            else:
                break



    elif key == '2':
    #let player use a consumable
        print("Use consumable.")

    elif key == '3':
    #let the player flee from the battle, gaining no experience 
        print("Flee!")
        Game.PrintMenu()


    else:
        print("Please select a valid option")

