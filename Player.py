import SkillPoints as Skills
import GameFunctions as Game

# PLAYER STATS #
level = 1
dmg = 1
xp = 0
hp = 100
mana = 100
hc = 0.75
dc = 0.05


gp = 0

#holds items and consumables
inventory = []

weapon = "Wooden Sword"
helmet = ""
chestplate = ""
gaunlets = ""
pants = ""
consumable = ""




def PrintInventory(): #print the player inventory
    print("Press 'I' to view your inventory.")
    key = input('')
    if key == 'I' or key == 'i':
        print(inventory)



def getGP():
    return gp

def setGP(x):
    gp = x



def Calc_Health():
    global hp
    hp = hp + (Skills[0][1] * 2)

def Calc_Mana():
    global mana
    mana = mana + (Skills[2][1] * 2)

def Calc_HitChance():
    global hc
    hc = hc + (Skills[1][1] / 100)

def Calc_Dodge():
    global dc
    dc = dc + (Skills[3][1] / 100)
