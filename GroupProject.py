#from breezypythongui import EasyFrame

import SkillPoints as Skills
import GameFunctions as Game

# Ideas

#maybe make this simpler that we originally planned?
#possibly do a single combat level to demonstrate using breezypythongui


#TO DO
#main menu
#key inputs to access other menus
#trader
#items
#weapons
#health bar/lives
#enemies
#levels
#finish skills effects
#inventory
#save data/progress
#player death
#semi perma death -> lose a few random items and some gold in the inventory upon death -> allow equipped items?

#possible weapon types: wooden sword, iron sword, copper sword, diamond sword
#possible helmet types: none, wooden helmet, iron helmet, copper helmet, diamond helmet
#possible chesplate types: none, wooden chestplate, iron chestplate, copper chestplate, diamond chestplate
#possible gauntlet types: none, padded gauntlet, armored gauntlet, armored gauntlet +
#possible pant types: none, padded pantss, armored pants, armored pants +
#possible consumables: health potions, mana potions, food



# GENERIC FUNCTIONS #


        
# insert method to show skills on request -> we could keep this as the 'S' key: only open while not in combat -> yes do this
# if keypress then show skill tree
# only allow skill tree while out of combat/in menus



# SKILL POINTS #

#specialAbility = [["1 - Strength: ", 0], ["2 - Dexterity: ", 0], ["3 - Intelligence: ", 0], ["4 - Agility: ", 0], ["5 - Stamina: ", 0]]

Skills.CreateSaveFile()

Skills.LoadSkills()



# END SKILL POINTS #



# SKILL EFFECTS #



'''Calc_Health()
Calc_Mana()
Calc_HitChance()
Calc_Dodge()'''



# END SKILL EFFECTS #

        

# DUNGEON #

#Enemy types
enemies = [["Grunt", 10, 2], ["Goblin", 15, 5], ["Zombie", 22, 9], ["Skeleton", 30, 12], ["Wizard", 42, 19]] #find a way to automaticall increase difficulty based on level, skills, and armor
enemy = "Grunt"



#example: if total health > 15, zombies start spawning. if total health > 25, skeletons start spawning

# END DUNGEON #



# TRADER #


# END TRADER #



# GAME LOGIC #

Game.PrintMenu()



