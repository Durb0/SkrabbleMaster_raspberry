import keyboard
from components import AnalyseComponent, PartyComponent, ValidationComponent
from components.validation import Choice
from service.componentservice import ComponentService
from service.turn import TurnService
from service.board import Board
from core.inject import inject
from config import LONG_PRESS_TIME
import time

@inject('_board', Board)
@inject('_routing', ComponentService)
@inject('_turns', TurnService)
class SkrabbleMaster:

    def __init__(self):
        self._routing.setComponent(PartyComponent())
        self._board.mode_button.on_press.connect(self.handleModeButtonOnPress)
        # keyboard.on_press_key('l', lambda e: print(self._board.mode_button.isLight())) #TEMP à supprimer lorsqu'on aura un bouton lumineux fonctionnel


    def handleModeButtonOnPress(self, e):
        if e >= LONG_PRESS_TIME:
            self._routing.setComponent(
                ValidationComponent('Confirmer suppression cache?', '',
                                    Choice('Oui', lambda : self.clean(True)),
                                    Choice('Non', lambda : self.clean(False))
                )
            )
        else:
            if isinstance(self._routing.getComponent(), AnalyseComponent):
                self._routing.setComponent(PartyComponent())
                self._board.mode_button.setLight(True)
            else:
                self._routing.setComponent(AnalyseComponent())
                self._board.mode_button.setLight(False)

    def clean(self, choice):
        if choice:
            self._turns.cleanCache()
        self._routing.setComponent(PartyComponent())





if __name__ == '__main__':
    sm = SkrabbleMaster()
    while True:
        time.sleep(1) # keep the main thread running
