from os import system, name
from os.path import exists
from time import sleep
import array as array
import random


# Ideas

#skills effect combat
#strength - damage  & health?
# agility - dodge
# intelligence - abilities/magic?
# dexterity - weapon type/level? hit chance?
#endurance - extra turn? rate you lose mana/energy
#energy required to attack?
#special ability? choice at the beginning btw a selcect amount of specific abilities (extra health, extra strength, extra agility, etc)
#assign name to player/character?



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

def PrintMenu():
    print("Enter 'S' to view your skill points")
    print("Enter 'T' to talk to the trader")
    print("Enter 'D' to enter the dungeon")
    print("Enter 'X' to close the menu.")
    print("Enter 'Z' to close the game.")

    key = input("")
    
    if key == "S":
        PrintSkills()
        if sp > 0:
            print("Enter 'U' to spend skill points")
            key = input("")
            if key == "U":
                UpgradeSkills()
                
    if key == "D":
        print("Dungeon")
        #enter dungeon
    if key == "T":
        #enter trader
        #load trader inventory from file
        #after x time, refresh with new items
        GenerateTraderInv()
        for i in traderInventory:
            print(i)

    if key == 'X':
        #close the PrintMenu
        print("Closing menu...")

    if key == "Z":
        #close the game
        print("Closing game...")

# PLAYER STATS #
level = 1
xp = 0
hp = 100
mana = 100
hc = 0.75
dc = 0.05

# SKILL POINTS #
sp = 5

#need to implement max level
#max level = 25

skills = [["1 - Strength: ", 0], ["2 - Dexterity: ", 0], ["3 - Intelligence: ", 0], ["4 - Agility: ", 0], ["5 - Stamina: ", 0]]
specialAbility = [["1 - Strength: ", 0], ["2 - Dexterity: ", 0], ["3 - Intelligence: ", 0], ["4 - Agility: ", 0], ["5 - Stamina: ", 0]]

#Only works in terminal, not IDLE shell
def ClearTerminal():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
        
# insert method to show skills on request
# if keypress then show skill tree
# only allow skill tree while out of combat/in menus

def CreateSaveFile():
    if not exists("Test.txt"):
        file = open("Test.txt", "x")
        file.close()
CreateSaveFile()

# WIP
#working on proper file save format for easier read to store in variable skills
def SaveSkills():
    file = open("Test.txt", "w")
    for i in skills:
        file.write(str(i).replace("[", "").replace("'", "").replace("]", ","))
    file.close()

#need to also load skills by reading from file

#trying to read data from file and import to skills
#also add for special ability that player chose if we decide to add this
def LoadSkills():
    file = open("Test.txt", "r")
    for line in file.readlines():
        print(line.split(","))
    file.close()
LoadSkills()

def PrintSkills():
    ClearTerminal()
    for i in skills:
        for k in i:
            print(k, end = "")
        print()
    print("Available skill points: ", sp)

def UpgradeSkills():
    global sp
    
    while sp > 0:
        upgrade = input("Skill to upgrade: ")
        if upgrade == "E":
            PrintMenu()
            break
        else:
            upgrade = int(upgrade)
            upgrade -= 1
            if (upgrade >= 0 & upgrade <= 5):
                skills[upgrade][1] += 1
                sp -= 1
                SaveSkills()
                PrintSkills()

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

Calc_Health()
Calc_Mana()
Calc_HitChance()
Calc_Dodge()

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

#possible weapon types: wooden sword, iron sword, copper sword, diamond sword
#possible helmet types: none, wooden helmet, iron helmet, copper helmet, diamond helmet
#possible chesplate types: none, wooden chestplate, iron chestplate, copper chestplate, diamond chestplate
#possible gauntlet types: ????
#possible pant types: ????
#possible consumables: ????

# DUNGEON #

#Enemy types
enemies = [["Goblin", 15, 5], ["Zombie", 22, 9], ["Skeleton", 30, 12]] #find a way to automaticall increase difficulty based on level, skills, and armor
#example: if total health > 15, zombies start spawning. if total health > 25, skeletons start spawning

# END DUNGEON #

# TRADER #

#trader resets every 15 minutes?
#need to save trader inventory to file so it is not refreshed every time the player enters the trader

#inventory needs to be randomized
#should trader sell at least one of each equipment at any given time?
#ability to sell to trader?
traderInventory = []

def GenerateRandomItem():
    items = ["Weapon", "Helmet", "Chestplate", "Gauntlet", "Pants", "Consumable"] #only allow random items that are none or wooden for weapon, helmet, chestplate, and pants -- make gauntlet and consumables similar 
    item = random.choice(items)
    return item
    
def GenerateTraderInv(): #trader can have any items that are listed above, chooses 1 or 2 randomly from each list? or we can show them all
    global traderInventory
    while len(traderInventory) < 10:
        traderInventory.append(GenerateRandomItem())

# END TRADER #

# GAME LOGIC #

PrintMenu()
