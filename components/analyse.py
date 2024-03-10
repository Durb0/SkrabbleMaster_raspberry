from core.component import Component
from service.board import Board

from core import inject

@inject('_board',Board)
class AnalyseComponent(Component):

    def onInit(self):
        print('mode analyse')
        light = self._board.mode_button.setLight(False)
        assert not light

    def handleActionButtonOnPress(self, e):
        print('[A] action button pressed')