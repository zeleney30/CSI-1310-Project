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
enemies = [["Grunt", 10, 2], ["Goblin", 25, 5], ["Zombie", 40, 9], ["Skeleton", 55, 12], ["Wizard", 70, 19]] #find a way to automatically increase difficulty based on level, skills, and armor
enemy = '' #will be updated based on what enemy is suitable for the player


dunOptions = {'1': 'Fight', '2': 'Flee'}#, '3': 'Use Consumable'}



#defining characterists of each enemy for fights
for enemies[0] in enemies:
    enemy = enemies[0]
    enemyName = "Grunt"
    enemyhp = 10
    enemydmg = 2
for enemies[1] in enemies:
    enemy = enemies[1]
    enemyName = "Goblin"
    enemyhp = 25
    enemydmg = 5
for enemies[2] in enemies:
    enemy = enemies[2]
    enemyName = "Zombie"
    enemyhp = 40
    enemydmg = 9
for enemies[3] in enemies:
    enemy = enemies[3]
    enemyName = "Skeleton"
    enemyhp = 55
    enemydmg = 12
for enemies[4] in enemies:
    enemy = enemies[4]
    enemyName = "Wizard"
    enemyhp = 70
    enemydmg = 19

#determine the enemy based on player stats
def GenerateEnemy():
    if Player.dmg < 5:
        enemy == enemies[0]
        print("A " + enemyName + " appeared!")
        print(dunOptions)
    elif Player.dmg > 5 and Player.dmg < 10:
        enemy == enemies[1]
        print("A " + enemyName + " appeared!")
        print(dunOptions)
    elif Player.dmg > 10 and Player.dmg < 15:
        enemy == enemies[2]
        print("A " + enemyName + " appeared!")
        print(dunOptions)
    elif Player.dmg > 15 and Player.dmg < 20:
        enemy == enemies[3]
        print("A " + enemyName + " appeared!")
        print(dunOptions)
    elif Player.dmg > 20:
        enemy == enemies[4]
        print("A " + enemyName + " appeared!")
        print(dunOptions)
    else: 
        enemy == enemies[0]
        print("A " + enemyName + " appeared!")
        print(dunOptions)

    key = input("Please select an option from the above list: ")
 
    if key == '1':
        #fight the enemy
        if enemy == enemies[0]:
            print("Fight!")
            while Player.hp > 0:
                Player.hp = Player.hp - enemydmg
                enemyhp = enemyhp - Player.dmg
                if enemyhp <= 0:
                    print("You win! Gained 10 xp and 25 gold from this fight.")
                    Player.xp = Player.xp + 10
                    Player.getGP
                    Player.gp = Player.gp + 25
                    break
                elif Player.hp <= 0:
                    Player.xp = Player.xp + 2
                    Player.getGP
                    Player.gp = Player.gp + 5
                    print("You lose! Gained 2 xp and 5 gold from this fight.")
                    break
        elif enemy == enemies[1]:
            while Player.hp > 0:
                Player.hp = Player.hp - enemydmg
                enemyhp = enemyhp - Player.dmg
                if enemyhp <= 0:
                    print("You win! Gained 20 xp and 35 gold from this fight.")
                    Player.xp = Player.xp + 20
                    Player.getGP
                    Player.gp = Player.gp + 35
                    break
                elif Player.hp <= 0:
                    Player.xp = Player.xp + 4
                    Player.getGP
                    Player.gp = Player.gp + 5
                    print("You lose! Gained 4 xp and 5 gold from this fight.")
                    break
        elif enemy == enemies[2]:
            while Player.hp > 0:
                Player.hp = Player.hp - enemydmg
                enemyhp = enemyhp - Player.dmg
                if enemyhp <= 0:
                    print("You win! Gained 30 xp and 45 gold from this fight.")
                    Player.xp = Player.xp + 30
                    Player.getGP
                    Player.gp = Player.gp + 45
                    break
                elif Player.hp <= 0:
                    Player.xp = Player.xp + 6
                    Player.getGP
                    Player.gp = Player.gp + 5
                    print("You lose! Gained 6 xp and 5 gold from this fight.")
                    break
        elif enemy == enemies[3]:
            while Player.hp > 0:
                Player.hp = Player.hp - enemydmg
                enemyhp = enemyhp - Player.dmg
                if enemyhp <= 0:
                    print("You win! Gained 40 xp and 55 gold from this fight.")
                    Player.xp = Player.xp + 40
                    Player.getGP
                    Player.gp = Player.gp + 55
                    break
                elif Player.hp <= 0:
                    Player.xp = Player.xp + 8
                    Player.getGP
                    Player.gp = Player.gp + 5
                    print("You lose! Gained 8 xp and 5 gold from this fight.")
                    break
        elif enemy == enemies[4]:
            while Player.hp > 0:
                Player.hp = Player.hp - enemydmg
                enemyhp = enemyhp - Player.dmg
                if enemyhp <= 0:
                    print("You win! Gained 50 xp and 65 gold from this fight.")
                    Player.xp = Player.xp + 50
                    Player.getGP
                    Player.gp = Player.gp + 65
                    break
                elif Player.hp <= 0:
                    Player.xp = Player.xp + 10
                    Player.getGP
                    Player.gp = Player.gp + 5
                    print("You lose! Gained 10 xp and 5 gold from this fight.")
                    break


    #player flees -> allows them to go back and do other things from the main menu
    elif key == '2':
    #let the player flee from the battle, gaining no experience 
        print("Flee! You gained 0 xp and 0 gold for fleeing the fight.")


    ##player uses consumable 
    #elif key == '3':
    #let player use a consumable
        #print("Use consumable.")


    else:
        print("Please select a valid option")

