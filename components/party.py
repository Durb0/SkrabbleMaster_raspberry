from core.component import Component
from .validation import ValidationComponent, Choice
from service.componentservice import ComponentService
from service.board import Board
from service.turn import TurnService
from core.inject import inject
from models.turn import Turn
from components.utils import header
import random

@inject('_routing', ComponentService)
@inject('_turn', TurnService)
class PartyComponent(Component):

    def onInit(self):
        print('mode party')
        light = self._board.mode_button.setLight(True)
        assert light

    def setTemplate(self):
        cursor = 0
        head, cursor = header("Party", cursor)
        body = self.turnTemplate(cursor)

        return head + body

    def turnTemplate(self, y_start=20):
        template = []
        for index, turn in enumerate(self._turn.getTurns()):
            template.append("text?value={};color=0xFFFF;size=1;x_start=0;y_start={};".format("{}. {}".format(index+1,turn.entry), y_start + 10*index))
        return template

    def randomWord(self):
        # return a random Stringof 7 letters
        word = ""
        for i in range(7):
            word += chr(random.randint(65, 90))
        return word

    def handleActionButtonOnPress(self, duration):
        if duration >= 2:
            self._turn.removeLastTurn()
            self.change.emit()
        else:
            print('[TODO] Take a photo')
            print("[TODO] Analyse photo to get text")
            text = self.randomWord()
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
