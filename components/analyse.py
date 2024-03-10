from core.component import Component
from service import Board, TurnService

from core import inject

@inject('_board',Board)
@inject('_turn', TurnService)
class AnalyseComponent(Component):

    def onInit(self):
        light = self._board.mode_button.setLight(False)
        assert not light
        self.turns = self._turn.getTurns()
        self.index = 0

    @property
    def selected_turn(self):
        return self.turns[self.index]

    def show(self):
        if self.turns:
            print(self.selected_turn.entry)
            print([f'{i+1}. {solution.word} - {solution.score}' for i, choice in enumerate(self.selected_turn.solutions)])
        else:
            print('No turn to show')


    def handleActionButtonOnPress(self, e):
        if e >= 2:
            self.index = (self.index - 1) % len(self.turns)
        else:
            self.index = (self.index + 1) % len(self.turns)
        self.change.emit()
