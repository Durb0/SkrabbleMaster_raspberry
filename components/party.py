from core.component import Component
from .validation import ValidationComponent, Choice
from service.componentservice import ComponentService

from service.board import Board
from core import inject

@inject('_board',Board)
@inject('_routing', ComponentService)
class PartyComponent(Component):

    def onInit(self):
        print('mode party')
        light = self._board.mode_button.setLight(True)
        assert light

    def handleActionButtonOnPress(self, duration):
        if duration >= 1:
            print('[TODO] Remove last turn')
        else:
            print('[TODO] Take a photo')
            print("[TODO] Analyse photo to get text")
            text = "PAQUETA"
            print("[TODO] Show text on screen")
            print("[TODO] Wait for user to validate text")
            self._routing.setComponent(
                ValidationComponent('Do you valid the text?', text,
                            Choice('Yes', lambda : self.handleChoose('yes')),
                            Choice('No', lambda : self.handleChoose('no'))
                )
            )

    def handleChoose(self, choice):
        if choice == "yes":
            print('[TODO] Add turn')
        self._routing.setComponent(PartyComponent())