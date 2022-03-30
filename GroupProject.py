from os import system, name
from os.path import exists
import os
from time import sleep
import random
#from breezypythongui import EasyFrame

import SkillPoints as Skills
import GameFunctions as Game

# Ideas

#maybe make this simpler that we originally planned?
#possibly do a single combat level to demonstrate using breezypythongui


#TO DO
#main menu
#key inputs to access other menus
#shops
#items
#weapons
#health bar/lives
#enemies
#levels
#finish skills
#inventory
#save data/progress
#player death
#semi perma death -> lose a few random items and some gold in the inventory upon death -> allow equipped items?
#define main() so we can organize and call functions as they are needed






# PLAYER STATS #
level = 1
xp = 0
hp = 100
mana = 100
hc = 0.75
dc = 0.05


#need to implement max level
#max level = 25






# GENERIC FUNCTIONS #


        
# insert method to show skills on request -> we could keep this as the 'S' key: only open while not in combat -> yes do this
# if keypress then show skill tree
# only allow skill tree while out of combat/in menus



# SKILL POINTS #

#specialAbility = [["1 - Strength: ", 0], ["2 - Dexterity: ", 0], ["3 - Intelligence: ", 0], ["4 - Agility: ", 0], ["5 - Stamina: ", 0]]

Skills.CreateSaveFile()

Skills.LoadSkills()



# END SKILL POINTS #



# SKILL EFFECTS #

def Calc_Health():
    global hp
    hp = hp + (skills[0][1] * 2)

def Calc_Mana():
    global mana
    mana = mana + (skills[2][1] * 2)

def Calc_HitChance():
    global hc
    hc = hc + (skills[1][1] / 100)

def Calc_Dodge():
    global dc
    dc = dc + (skills[3][1] / 100)

'''Calc_Health()
Calc_Mana()
Calc_HitChance()
Calc_Dodge()'''

#need to calculate damage
#need to add endurance somehow
#need to make intelligence effect magic damage

# END SKILL EFFECTS #



#holds items and consumables
inventory = []

weapon = "Wooden Sword"
helmet = ""
chestplate = ""
gaunlets = ""
pants = ""
consumable = ""

def PrintInventory():
    print("Press 'I' to view your inventory.")
    if key == 'I' or key == 'i':
        print(inventory)
        

#possible weapon types: wooden sword, iron sword, copper sword, diamond sword
#possible helmet types: none, wooden helmet, iron helmet, copper helmet, diamond helmet
#possible chesplate types: none, wooden chestplate, iron chestplate, copper chestplate, diamond chestplate
#possible gauntlet types: none, padded gauntlet, armored gauntlet, armored gauntlet +
#possible pant types: none, padded pantss, armored pants, armored pants +
#possible consumables: ????

# DUNGEON #

#Enemy types
enemies = [["Grunt", 10, 2], ["Goblin", 15, 5], ["Zombie", 22, 9], ["Skeleton", 30, 12], ["Wizard", 42, 19]] #find a way to automaticall increase difficulty based on level, skills, and armor
enemy = "Grunt"



#example: if total health > 15, zombies start spawning. if total health > 25, skeletons start spawning

# END DUNGEON #



# TRADER #

#trader resets every XX minutes? 15? 5?
#need to save trader inventory to file so it is not refreshed every time the player enters the trader

#inventory needs to be randomized
#should trader sell at least one of each equipment at any given time? --> player should have option to decline buying anything -> yes, if the player doesnt like the options they can leave the trader
#ability to sell to trader? --> only if it isnt a pain in the ass -> agreed but shouldnt be hard
traderHelmets = ["None", "Wooden Helmet", "Iron Helmet", "Copper Helmet", "Diamond Helmet"]
traderChestplates = ["None", "Wooden Chestplate", "Iron Chestplate", "Copper Chestplate", "Diamond Chestplate"]
traderGauntlets = ["None", "Padded Gauntlet", "Armored Gauntlet", "Armored Gauntlet +"]
traderPants = ["None", "Padded Pants", "Armored Pants", "Armored Pants +"]
traderConsumables = [""]
traderInventory = [""] #randomly generate trader inventory from above lists

def GenerateRandomItem():
    items = ["Weapon", "Helmet", "Chestplate", "Gauntlet", "Pants", "Consumable"] #only allow random items that are none or wooden for weapon, helmet, chestplate, and pants -- make gauntlet and consumables similar 
    items = random.choice(traderHelmets, k=2) + random.choice(traderChestplates, k=2) + random.choice(traderGauntlets, k=2) + random.choice(traderPants, k=2)
    return items
    
def GenerateTraderInv(): #generates 2 of each item for the trader to have available to buy
    global traderInventory
    traderInventory = random.choice(traderHelmets, k=2) + random.choice(traderChestplates, k=2) + random.choice(traderGauntlets, k=2) + random.choice(traderPants, k=2)
    while len(traderInventory) < 10:
        traderInventory.append(GenerateRandomItem())
        return traderInventory
    else:
        traderInventory = random.choice(traderHelmets, k=2) + random.choice(traderChestplates, k=2) + random.choice(traderGauntlets, k=2) + random.choice(traderPants, k=2)
        return traderInventory

# END TRADER #



# GAME LOGIC #

Game.PrintMenu()



