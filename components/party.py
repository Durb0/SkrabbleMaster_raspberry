from core.component import Component
from .validation import ValidationComponent, Choice
from service import ComponentService, Board, TurnService
from core import inject
from models.turn import Turn

@inject('_board',Board)
@inject('_routing', ComponentService)
@inject('_turn', TurnService)
class PartyComponent(Component):

    def onInit(self):
        print('mode party')
        light = self._board.mode_button.setLight(True)
        assert light

    def show(self):
        for turn in self._turn.getTurns():
            print(turn.entry)

    def handleActionButtonOnPress(self, duration):
        if duration >= 2:
            self._turn.removeLastTurn()
        else:
            print('[TODO] Take a photo')
            print("[TODO] Analyse photo to get text")
            text = "PAQUETA"
            self._routing.setComponent(
                ValidationComponent('Do you valid the text?', text,
                            Choice('Yes', lambda : self.handleChoose('yes', text)),
                            Choice('No', lambda : self.handleChoose('no', text))
                )
            )

    def handleChoose(self, choice, text):
        if choice == "yes":
            self._turn.addTurn(Turn(text,[]))
            self.change.emit()
        self._routing.setComponent(PartyComponent())