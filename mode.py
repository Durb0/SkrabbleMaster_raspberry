from enum import Enum
from abc import ABC, abstractmethod

class Subscription():
    def __init__(self, listener, action):
        self.listener = listener
        self.action = action
        self.listener.connect(self.action)

    def disconnect(self):
        self.listener.disconnect(self.action)

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

    def handleActionButtonOnPress(self, e):
        pass

class ModeAnalyse(Mode):

    def __init__(self):
        super().__init__(ModeType.ANALYSE)

    def onSetContext(self):
        print('mode analyse')
        light = self.context.board.mode_button.setLight(False)
        assert not light

    def handleActionButtonOnPress(self, e):
        print('[A] action button pressed')


class ModeParty(Mode):

    def __init__(self):
        super().__init__(ModeType.PARTY)

    def onSetContext(self):
        print('mode party')
        light = self.context.board.mode_button.setLight(True)
        assert light

    def handleActionButtonOnPress(self, e):
        print('[P] action button pressed')