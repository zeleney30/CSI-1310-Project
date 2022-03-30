from os import system, name
from os.path import exists
import os
import random

#trader resets every XX minutes? 15? 5?

#need to add gp value associated with each item

#inventory needs to be randomized
#should trader sell at least one of each equipment at any given time? --> player should have option to decline buying anything -> yes, if the player doesnt like the options they can leave the trader
#ability to sell to trader? --> only if it isnt a pain in the ass -> agreed but shouldnt be hard
traderWeapons = ["Wooden Sword", "Iron Sword", "Copper Sword", "Diamond Sword"]
traderHelmets = ["Wooden Helmet", "Iron Helmet", "Copper Helmet", "Diamond Helmet"]
traderChestplates = ["Wooden Chestplate", "Iron Chestplate", "Copper Chestplate", "Diamond Chestplate"]
traderGauntlets = ["Padded Gauntlet", "Steel Gauntlet"]
traderPants = ["Padded Pants", "Iron Pants"]
traderConsumables = ["Health Potion", "Mana Potion", "Food"]
traderInventory = [] #randomly generated trader inventory from above lists

#Create the save file if it doesnt already exist
def CreateSaveFile():
    if not exists("Trader.txt"):
        file = open("Trader.txt", "x")
        file.close()

#Save trader
def Save():
    file = open("Trader.txt", "w")
    for i in traderInventory:
        file.write(str(i) + "\n")
        
    file.close()

#Load trader
def Load():
    if not os.path.getsize("Trader.txt") > 0:
        return
    
    global traderInventory

    file = open("Trader.txt", "r")

    i = 0

    while True:
        i += 1

        line = file.readline()

        if not line:
            break

        traderInventory.insert(i, line.strip())

    file.close()



#Generate a random item
def GenerateRandomItem():
    items = ["Weapon", "Helmet", "Chestplate", "Gauntlet", "Pants", "Consumable"] #match item level to player level, for example, if player is level 1 generate wooden or iron, not diamond

    itemType = random.choice(items) #Choose a random category

    if (itemType == "Weapon"):
        item = random.choice(traderWeapons) #need to add weapon categories, bow, staff, mace, sword, etc
    elif (itemType == "Helmet"):
        item = random.choice(traderHelmets)
    elif (itemType == "Chestplate"):
        item = random.choice(traderChestplates)
    elif (itemType == "Gauntlet"):
        item = random.choice(traderGauntlets)
    elif (itemType == "Pants"):
        item = random.choice(traderPants)
    elif (itemType == "Consumable"):
        item = random.choice(traderConsumables)
    
    return item

#Generate a random inventory for the trader to sell to the player
def GenerateTraderInv():
    global traderInventory

    i = 0
    
    while len(traderInventory) < 10:    #Trader's inventory is 10 items long
        traderInventory.insert(i, GenerateRandomItem())
        i += 1

    Save()

    return traderInventory

def getInventory():
    return traderInventory
