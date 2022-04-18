from os import system, name
from os.path import exists
import os

import GameFunctions as Game

#Initialize skill variables (If there is no save file then this is a new game, use these values)
sp = 5
skills = [["1 - Strength: ", 0], ["2 - Dexterity: ", 0], ["3 - Intelligence: ", 0], ["4 - Agility: ", 0], ["5 - Stamina: ", 0]]

def playerSkills():
    print(skills, "Skills")
    print(sp, "Your remaining skill points: ")

def getSP():
    return sp

def setSP(x):
    sp = x

#Create the save file if it doesnt already exist
def CreateSaveFile():
    if not exists("Skills.txt"):
        file = open("Skills.txt", "x")
        file.close()

#Save skills
def Save():
    file = open("Skills.txt", "w")
    for i in skills:
        for k in i:
            file.write(str(k) + "\n")

    file.write(str(sp) + "\n")
    file.close()

#Load skills
def Load():
    if not os.path.getsize("Skills.txt") > 0:
        return
    
    global skills
    global sp
    
    file = open("Skills.txt", "r")
    
    list1 = []
    list2 = []

    i = 0

    while True:
        i += 1

        line = file.readline()

        if not line:
            break

        if not (i == 11):
            if (i % 2) == 1:
                list1.insert(i, line.strip() + " ")
            else:
                list2.insert(i, int(line.strip()))
        else:
            sp = int(line.strip())
    
    file.close()

    list3 = []

    j = 0

    while j < len(list1):
        list3.insert(j, [list1[j], list2[j]])
        j += 1

    skills = list3     

Load()

#Print skills
def PrintSkills():
    Game.ClearTerminal()
    for i in skills:
        for k in i:
            print(k, end = "")
        print()
    print("Available skill points: ", sp)
    
    if sp > 0:
        print("Enter 'U' to spend skill points")
        
    key = input("")
    
    if key == "U" or key == "u":
        UpgradeSkills()
    elif key == "E" or key == "e":
        Game.PrintMenu()

#Upgrade skills
def UpgradeSkills():
    global sp
    
    while sp > 0:
        if sp <= 0:
            PrintSkills()
            break
            
        upgrade = input("Skill to upgrade: ")
        
        if upgrade == "E" or upgrade == 'e':
            PrintSkills()
            break
        else:
            upgrade = int(upgrade)
            upgrade -= 1
            if (upgrade >= 0 & upgrade <= 5):
                skills[upgrade][1] += 1
                sp -= 1
                Save()
                PrintSkills()
    
