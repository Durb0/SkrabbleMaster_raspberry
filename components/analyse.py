from core.component import Component
from service.turn import TurnService

from core.inject import inject
from components.utils import header
from config import LONG_PRESS_TIME

@inject('_turn', TurnService)
class AnalyseComponent(Component):

    def onInit(self):
        light = self._board.mode_button.setLight(False)
        assert not light

    def setTemplate(self):
        cursor = 0
        head, cursor = header("Analyse", cursor)
        turn = self._turn.selected_turn

        if not turn:
            return head + ["text?value=No turn found;color=0xFFFF;size=2;x_start=0;y_start={};".format(cursor)]
        body = self.turnTemplate(cursor, turn)
        return head + body

    def turnTemplate(self, cursor, turn):
        template = []
        template.append("text?value={}. {};color=0xFFFF;size=4;x_start=0;y_start={};".format(self._turn.selected_index+1, turn.entry, cursor))
        cursor += 40
        for i in range(4):
            solution = turn.solutions[i]
            template.append("text?value=-- {} --\n {};color=0xFFFF;size=2;x_start=0;y_start={};".format(solution.score, ", ".join(solution.words[:4]), cursor + 50*i))
            i += 1
        return template

    def handleActionButtonOnPress(self, e):
        if e >= LONG_PRESS_TIME:
            self._turn.previousIndex()
        else:
            self._turn.nextIndex()
        self.change.emit()
