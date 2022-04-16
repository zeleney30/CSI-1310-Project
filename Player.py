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


#need to implement max level
#max level = 25

gp = 100000

#holds items and consumables
inventory = []

weapon = "Wooden Sword"
helmet = ""
chestplate = ""
gauntlets = ""
pants = ""



#Create the save file if it doesnt already exist
def CreateSaveFile():
    if not exists("Inventory.txt"):
        file = open("Inventory.txt", "x")
        file.close()

#Save trader
def Save():
    file = open("Inventory.txt", "w")

    file.write(weapon + "\n")
    file.write(helmet + "\n")
    file.write(chestplate + "\n")
    file.write(gauntlets + "\n")
    file.write(pants + "\n")
    
    for i in inventory:
        file.write(str(i) + "\n")
        
    file.close()
    
#Load trader
def Load():
    if not os.path.getsize("Inventory.txt") > 0:
        return
    
    global inventory
    global weapon
    global helmet
    global chestplate
    global gauntlets
    global pants

    file = open("Inventory.txt", "r")

    i = 0

    while True:
        i += 1

        line = file.readline()

        if not line:
            break

        print(line)

        if i == 1:
            weapon = line.strip()
        if i == 2:
            helmet = line.strip()
        if i == 3:
            chestplate = line.strip()
        if i == 4:
            gauntlets = line.strip()
        if i == 5:
            pants = line.strip()

        inventory.insert(i, line.strip())

    file.close()



def PrintInventory():
    print("Equipped:")
    if weapon != "":
        print(weapon)

    if helmet != "":
        print(helmet)

    if chestplate != "":
        print(chestplate)

    if gauntlets != "":
        print(gauntlets)

    if pants != "":
        print(pants)
        
    print("")
    
    count = 1
    
    for i in inventory:
        print(str(count) + " - " + i)
        count += 1



def EquipItem():
    PrintInventory()
    print("Item to equip: ")

    key = input('')

    item = inventory[int(key) - 1]

    global weapon
    global helmet
    global chestplate
    global gauntlets
    global pants

    if "Sword" in item:
        if weapon != "":
            temp = item
            inventory[int(key) - 1] = weapon
            weapon = temp
        else:
            weapon = item
            inventory.remove(item)

    if "Helmet" in item:
        if helmet != "":
            temp = item
            inventory[int(key) - 1] = helmet
            helmet = temp
        else:
            helmet = item
            inventory.remove(item)

    if "Chestplate" in item:
        if chestplate != "":
            temp = item
            inventory[int(key) - 1] = chestplate
            chestplate = temp
        else:
            chestplate = item
            inventory.remove(item)

    if "Gauntlet" in item:
        if gauntlets != "":
            temp = item
            inventory[int(key) - 1] = gauntlets
            gauntlets = temp
        else:
            gauntlets = item
            inventory.remove(item)

    if "Pants" in item:
        if pants != "":
            temp = item
            inventory[int(key) - 1] = pants
            pants = temp
        else:
            pants = item
            inventory.remove(item)

    Save()



def OpenInventory():
    print("Press 'I' to view your inventory.")
    print("Press 'E' to equip an item.")

    key = input('')
    
    if key == 'I' or key == 'i':
        PrintInventory()

    if key == 'E' or key == 'e':
        EquipItem()


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
