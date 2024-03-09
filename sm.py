from board import Board
from enum import Enum
from mode import ModeAnalyse, ModeParty, Mode, ModeType

class SkrabbleMaster:

    def __init__(self, mode:Mode = ModeAnalyse()):
        self.turns = []#TODO Créer la classe Turn
        self.board = Board()
        self.board.mode_button.on_press.connect(self.handleModeButton)
        self.set_mode(mode)

    def set_mode(self, mode:Mode):
        self.mode = mode
        self.mode.context = self

    def cleanCache(self):
        self.turns = []
        print('cache cleaned')

    def handleModeButton(self, e):
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