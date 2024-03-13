from service.board import Board
from enum import Enum
from models.turn import Turn
from typing import List
import keyboard
from components import Component, AnalyseComponent, PartyComponent, ValidationComponent
from service import ComponentService, TurnService, Board
from core.inject import inject

@inject('_board', Board)
@inject('_routing', ComponentService)
@inject('_turns', TurnService)
class SkrabbleMaster:

    def __init__(self):
        self._routing.setComponent(PartyComponent())
        self._board.mode_button.on_press.connect(self.handleModeButtonOnPress)
        keyboard.on_press_key('l', lambda e: print(self._board.mode_button.isLight())) #TEMP à supprimer lorsqu'on aura un bouton lumineux fonctionnel


    def handleModeButtonOnPress(self, e):
        if e >= 2:
            self._turns.cleanCache()
        else:
            if isinstance(self._routing.getComponent(), AnalyseComponent):
                self._routing.setComponent(PartyComponent())
            else:
                self._routing.setComponent(AnalyseComponent())




if __name__ == '__main__':
    sm = SkrabbleMaster()
    input('Press enter to exit')
    print('Exiting')