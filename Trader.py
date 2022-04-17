from os import system, name
from os.path import exists
import os
import random
from re import A

import GameFunctions as Game
import Player as Player


#need to add gp value associated with each item

#inventory needs to be randomized
#if the player doesnt like the options they can leave the trader, not required to buy anything
traderWeapons =     ["Tin Sword", "Copper Sword", "Steel Sword"]
traderHelmets =     ["Tin Helmet", "Copper Helmet", "Steel Helmet"]
traderChestplates = ["Tin Chestplate", "Copper Chestplate", "Steel Chestplate"]
traderGauntlets =   ["Tin Gauntlet", "Copper Gauntlet", "Steel Gauntlet"]
traderPants =       ["Tin Pants", "Copper Pants", "Steel Pants"]
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



def calcPrice(item): #calculate item prices
    item = ['']
    tier = 0
    gp = 0

    if "Tin" in item:
        tier = 1
    elif "Copper" in item:
        tier = 2
    elif "Steel" in item:
        tier = 3

    gp = random.randint(10 * (tier * tier), 20 * (tier * tier))

    return gp



def PrintTrader():
    Game.ClearTerminal()

    count = 1
    
    for i in getInventory():
        print(count, " - ", i)
        count += 1

    print("Press 'P' to purchase an item.")
    key = input('')


    if (key == "P" or key == 'p'):
        PurchaseItem()
    else:
        print("Please select a valid option.")

def PurchaseItem():

    price = 0 #calcPrice(item)

    key=input("Item to purchase: ")
    print("This item costs " + str(price) + " gold.")


    item = traderInventory[int(key) - 1]

    

    if (Player.getGP() >= price):
        Player.setGP(Player.getGP() - price)
        Player.inventory.append(item)



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
