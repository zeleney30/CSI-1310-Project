# PLAYER STATS #
level = 1
xp = 0
hp = 100
mana = 100
hc = 0.75
dc = 0.05


#need to implement max level
#max level = 25


#holds items and consumables
inventory = []

weapon = "Wooden Sword"
helmet = ""
chestplate = ""
gaunlets = ""
pants = ""
consumable = ""

#need to calculate damage
#need to add endurance somehow
#need to make intelligence effect magic damage

def PrintInventory():
    print("Press 'I' to view your inventory.")
    if key == 'I' or key == 'i':
        print(inventory)

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