from enum import Enum
from abc import ABC, abstractmethod

class ModeType(Enum):
    ANALYSE = 1
    PARTY = 2

class Mode(ABC):

    def __init__(self, mode:ModeType):
        self._context = None
        self.mode = mode

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context
        self.onSetContext()

    @abstractmethod
    def onSetContext(self):
        pass

class ModeAnalyse(Mode):

    def __init__(self):
        super().__init__(ModeType.ANALYSE)

    def onSetContext(self):
        print('mode analyse')
        light = self.context.board.mode_button.setLight(False)
        assert not light


class ModeParty(Mode):

    def __init__(self):
        super().__init__(ModeType.PARTY)

    def onSetContext(self):
        print('mode party')
        light = self.context.board.mode_button.setLight(True)
        assert light