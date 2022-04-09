from os import system, name
from os.path import exists
import os
import SkillPoints as Skills
import GameFunctions as Game
import Player as Player
import Enemies as Enemies
import GameFunctions as Game

def EnterDungeon():
    print("Entering dungeon...")
    Enemies.GenerateEnemy()


