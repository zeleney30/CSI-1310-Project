from os import system, name

import SkillPoints
import Trader as Trader
import Player as Player
import Dungeon as Dungeon
from breezypythongui import EasyFrame

class popupWindow(EasyFrame):
    """Displays a greeting in a window"""
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text = "Welcome to Mini Dungeon Simulator", row = 0, column = 0)
def main():
    popupWindow().mainloop()

main()

#Only works in terminal, not IDLE shell
def ClearTerminal():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

menu={'A': '- Continue Game', 'B':'- Quit Game'} #open automatically on game startup --> change to ONLY on startup or when asked for


def PrintMenu():
    if selection == 'A' or selection == 'a': #main menu for game, can be opened at tny time
        print("Enter 'S' to view your skill points")
        print("Enter 'T' to talk to the trader")
        print("Enter 'I' to view your inventory")
        print("Enter 'D' to enter the dungeon")
        print("Enter 'X' to close the menu.")
        print("Enter 'Z' to close the game.")

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
        PrintMenu()
        
    elif selection == 'B' or selection == 'b':
        #close the game -- autosave before closing
        print("Closing game...")
        quit()
   
    else:
        print("Please select a valid option.")
        #open the menu again so they can choose a valid option



    key = input("Please select one of the above menu items: ")


    #key = input("")
    
    if key == "S" or key == "s":
        #load skill menu
        #print skill menu
        SkillPoints.PrintSkills()
        

    if key == "E" or key == "e":
        print(menu)
                
    if key == "D" or key == "d":
        print("Dungeon")
        Dungeon.EnterDungeon()
        #enter dungeon


    if key == "T" or key == "t":
        #enter trader
        #load trader inventory from file
        #after x time, refresh with new items -- 15 minutes? 5 minutes?
        Trader.GenerateTraderInv()
        Trader.PrintTrader()

    if key == 'I' or key == 'i':
        #Open inventory
        print("Opening inventory...")
        Player.OpenInventory()

    if key == 'X' or key == 'x':
        #close the PrintMenu
        print("Closing menu...")
        

    if key == 'Z' or key == 'z':
        #close the game
        print("Closing game...")
        quit()


