from board import Board
from enum import Enum
from mode import ModeAnalyse, ModeParty, Mode, ModeType
from turn import Turn
from typing import List
import keyboard

class SkrabbleMaster:

    def __init__(self, mode:Mode = ModeAnalyse()):
        self.mode = None
        self.turns:List[Turn] = []
        self.board:Board = Board()
        
        self.board.mode_button.on_press.connect(self.handleModeButtonOnPress)
        self.board.action_button.on_press.connect(self.handleActionButtonOnPress)
        self.set_mode(mode)

        keyboard.on_press_key('l', lambda e: print(self.board.mode_button.isLight())) #TEMP à supprimer lorsqu'on aura un bouton lumineux fonctionnel

    def set_mode(self, mode:Mode):
        self.mode = mode
        self.mode.context = self


    def cleanCache(self):
        self.turns = []
        print('cache cleaned')

    def handleActionButtonOnPress(self, e):
        self.mode.handleActionButtonOnPress(e)

    def handleModeButtonOnPress(self, e):
        if e >= 2:
            self.cleanCache()
        else:
            if self.mode.mode == ModeType.ANALYSE:
                self.set_mode(ModeParty())
            else:
                self.set_mode(ModeAnalyse())




if __name__ == '__main__':
    sm = SkrabbleMaster()
    input('Press enter to exit')
    print('Exiting')