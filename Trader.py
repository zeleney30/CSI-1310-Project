import random

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
