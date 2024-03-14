from core.component import Component
from .validation import ValidationComponent, Choice
from service.componentservice import ComponentService
from service.board import Board
from service.turn import TurnService, MAX_TURNS
from service.anagram import AnagramService
from core.inject import inject
from models.turn import Turn
from components.utils import header
import random
from config import LONG_PRESS_TIME

@inject('_routing', ComponentService)
@inject('_turn', TurnService)
@inject('_anagram', AnagramService)
class PartyComponent(Component):

    def onInit(self):
        print('mode party')
        light = self._board.mode_button.setLight(True)
        assert light

    def setTemplate(self):
        cursor = 0
        head, cursor = header("Partie", cursor)
        body = self.turnsTemplate(cursor)

        return head + body

    def turnsTemplate(self, y_start=20):
        template = []
        i = 0
        for index, turn in enumerate(self._turn.turns):
            # get only the last 6 turns
            if len(self._turn.turns) > MAX_TURNS:
                if index < len(self._turn.turns) - MAX_TURNS:
                    continue
            template.append("text?value={}. {};color=0xFFFF;size=3;x_start=0;y_start={};".format(index+1, turn.entry, y_start + 30*i))
            i += 1
        return template

    def randomWord(self):
        # return a random Stringof 7 letters
        word = ""
        for i in range(7):
            word += chr(random.randint(65, 90))
        return word

    def handleActionButtonOnPress(self, duration):
        if duration >= LONG_PRESS_TIME:
            self._routing.setComponent(ValidationComponent('Annuler le dernier tour?', "",
                            Choice('Oui', lambda : self.handleRemove(True)),
                            Choice('Non', lambda : self.handleRemove(False))
            ))
        else:
            print('[TODO] Take a photo')
            print("[TODO] Analyse photo to get text")
            text = self.randomWord()
            self._routing.setComponent(
                ValidationComponent('Validez vous ce chevalet?', text,
                            Choice('Oui', lambda : self.handleChoose('yes', text)),
                            Choice('Non', lambda : self.handleChoose('no', text))
                )
            )

    def handleChoose(self, choice, text):
        if choice == "yes":
            self._routing.setComponent(ValidationComponent('', 'Patientez...', Choice('', lambda : None), Choice('', lambda : None)))
            turn = self._anagram.find_anagrams(text.lower())
            self._turn.addTurn(turn)
        self._routing.setComponent(PartyComponent())

    def handleRemove(self, choice):
        if choice:
            self._turn.removeLastTurn()
        self._routing.setComponent(PartyComponent())