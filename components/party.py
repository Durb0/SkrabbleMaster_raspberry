from .core import Component
from .validation import ValidationComponent, Choice

class PartyComponent(Component):

    def show(self):
        pass #TODO

    def __init__(self):
        super().__init__()

    def onSetContext(self):
        print('mode party')
        light = self.context.board.mode_button.setLight(True)
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
            self._context.set_component(
                ValidationComponent('Do you valid the text?', text,
                                Choice('Yes', lambda : self.handleChoose('yes')),
                                Choice('No', lambda : self.handleChoose('no'))
                )
            )

    def handleChoose(self, choice):
        if choice == "yes":
            print('[TODO] Add turn')
        self._context.set_component(PartyComponent())