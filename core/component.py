from abc import ABC, abstractmethod
from PySignal import Signal
from typing import List
from service.board import Board
from core.inject import inject

@inject('_board',Board)
class Component(ABC):

    template: List[str] = []

    def __init__(self):
        self.change = Signal()
        self.change.connect(self.handleChanges)
        self.onInit()
        self.template = self.setTemplate()
        self.show()

    @abstractmethod
    def setTemplate(self):
        return []

    def handleChanges(self):
        self.onChanges()
        self.show()

    def onChanges(self):
        pass

    def show(self):
        self._board.screen.show_on_arduino(self.template)

    def onInit(self):
        pass

    def handleActionButtonOnPress(self, e):
        pass