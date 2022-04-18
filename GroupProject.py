import GameFunctions as Game
import Player as Player
import SkillPoints as Skills
from breezypythongui import EasyFrame

class popupWindow(EasyFrame):
    """Displays a greeting in a window"""
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text = "Welcome to Mini Dungeon Simulator", row = 0, column = 0)
def main():
    popupWindow().mainloop()

main()


Skills.Load()

# GAME LOGIC #
Game.PrintMenu()



