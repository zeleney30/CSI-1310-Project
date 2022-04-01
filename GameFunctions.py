from os import system, name

import SkillPoints as Skills
import Trader as Trader

#Only works in terminal, not IDLE shell
def ClearTerminal():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

menu={'A': '- Continue Game', 'B': '- New Game', 'C':'- Save Game', 'D':'- Quit Game'} #open automatically on game startup

while True:
    options = menu.keys()
    for entry in options:
        print(entry, menu[entry])
        f = open("PythonGame.txt", 'w+')
        f.close()
        #write save data
        

    selection=input("Please select one of the following options: ")
    if selection == 'A' or selection == 'a':
        #load previous game
        print("Loading game...")
        break
    elif selection == 'B' or selection == 'b':
        #start new game
        f = open("Pythongame.txt", 'w+')
        f.truncate()
        f.close()
        print("Starting new game...")
        break
    elif selection == 'C' or selection == 'c':
        #save the game
        print("Saving game...")
        break
    elif selection == 'D' or selection == 'd':
        #close the game -- autosave before closing
        print("Closing game...")
        break
        quit()
        
    else:
        print("Please select a valid option.")
        #open the menu again so they can choose a valid option

def PrintMenu():
    if selection == 'A' or selection == 'a' or selection == 'B' or selection == 'b':
        print("Enter 'S' to view your skill points")
        print("Enter 'T' to talk to the trader")
        print("Enter 'D' to enter the dungeon")
        print("Enter 'X' to close the menu.")
        print("Enter 'Z' to close the game.")


    key = input("")
    
    if key == "S" or key == "s":
        Skills.PrintSkills()
        

        if key == "E" or key == "e":
            PrintMenu()
                
    if key == "D" or key == "d":
        print("Dungeon")
        #enter dungeon
    if key == "T" or key == "t":
        #enter trader
        #load trader inventory from file
        #after x time, refresh with new items -- 15 minutes? 5 minutes?
        Trader.GenerateTraderInv()
        Trader.PrintTrader()

    if key == 'X' or key == 'x':
        #close the PrintMenu
        print("Closing menu...")

    if key == 'Z' or key == 'z':
        #close the game
        print("Closing game...")
        quit()
