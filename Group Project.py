from os import system, name
from os.path import exists
import os
from time import sleep
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
#player death
#semi perma death -> lose a few random items and some gold in the inventory upon death -> allow equipped items?
#define main() so we can organize and call functions as they are needed

menu=[0,1,2] #open automatically on game startup
menu[0] = "Continue Game"
menu[1] = "Save Game"
menu[2] = "Quit Game"
while True:
    options = menu.keys()
    options.sort()
    for entry in options:
        print(entry, menu[entry])
        f=open("PythonGame.txt", 'r')

    selection=input("Please select one of the following options: ")
    if selection == 0 :
        #start the game
        print("Loading game...")
    elif selection == 1 :
        #write save to file
        print("Saving game...")
    elif selection == 2 :
        #close the game -- ask player to make sure they saved first!
        print("Closing game...")
        break
    else:
        print("Please select a valid option.")
        #open the menu again so they can choose a valid option


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
        #after x time, refresh with new items -- 15 minutes? 5 minutes?
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



# GENERIC FUNCTIONS #

#Only works in terminal, not IDLE shell
def ClearTerminal():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
        
# insert method to show skills on request -> we could keep this as the 'S' key: only open while not in combat -> yes do this
# if keypress then show skill tree
# only allow skill tree while out of combat/in menus

# SKILL POINTS #

# If the save file doesnt exist, create it #
# Should we use one file to store all the data? it might get messy
def CreateSaveFile():
    if not exists("Test.txt"):
        file = open("Test.txt", "x")
        file.close()
CreateSaveFile()

# Save skills to file #
def SaveSkills():
    file = open("Test.txt", "w")
    for i in skills:
        for k in i:
            file.write(str(k) + "\n")
    file.close()


#trying to read data from file and import to skills
#also add for special ability that player chose if we decide to add this
def LoadSkills():
    if not os.path.getsize("Test.txt") > 0:
        return
    
    global skills
    
    file = open("Test.txt", "r")
    
    list1 = []
    list2 = []

    i = 0

    while True:
        i += 1

        line = file.readline()

        if not line:
            break

        if (i % 2) == 1:
            list1.insert(i, line.strip() + " ")
        else:
            list2.insert(i, int(line.strip()))
    
    file.close()

    list3 = []

    j = 0

    while j < len(list1):
        list3.insert(j, [list1[j], list2[j]])
        j += 1

    skills = list3        
LoadSkills()

# Print skills to terminal #
def PrintSkills():
    ClearTerminal()
    for i in skills:
        for k in i:
            print(k, end = "")
        print()
    print("Available skill points: ", sp)

# Upgrade skill aspect and save to file #
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
#possible gauntlet types: none, padded gauntlet, armored gauntlet, armored gauntlet +
#possible pant types: none, padded pantss, armored pants, armored pants +
#possible consumables: ????

# DUNGEON #

#Enemy types
enemies = [["Grunt", 10, 2], ["Goblin", 15, 5], ["Zombie", 22, 9], ["Skeleton", 30, 12], ["Wizard", 42, 19]] #find a way to automaticall increase difficulty based on level, skills, and armor
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

PrintMenu()
