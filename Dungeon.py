from os import system, name
from os.path import exists
import os
import SkillPoints as Skills
import GameFunctions as Game
import Player as Player
import Enemies as Enemies
import GameFunctions as Game

def EnterDungeon(): #starts a fight sequence that will run in enemies
    try: 
        print("Entering dungeon...")
        Enemies.GenerateEnemy()
    except:
        print("Something went wrong! Try re-launching game.")


