from core.component import Component
from service.turn import TurnService

from core.inject import inject
from components.utils import header

@inject('_turn', TurnService)
class AnalyseComponent(Component):

    def onInit(self):
        light = self._board.mode_button.setLight(False)
        assert not light
        self.turns = self._turn.getTurns()
        self.index = 0

    def setTemplate(self):
        cursor = 0
        head, cursor = header("Analyse", cursor)

        body = ["text?value={};color=0xFFFF;size=2;x_start=0;y_start={};".format(turn.entry, 20 + 20*index) for index, turn in enumerate(self.turns)]

        # fusion head and body
        return head + body

    @property
    def selected_turn(self):
        return self.turns[self.index]

    def handleActionButtonOnPress(self, e):
        if e >= 2:
            self.index = (self.index - 1) % len(self.turns)
        else:
            self.index = (self.index + 1) % len(self.turns)
        self.change.emit()
