from abc import ABC, abstractmethod
from PySignal import Signal

class Component(ABC):

    def __init__(self):
        self.change = Signal()
        self.change.connect(self.handleChanges)
        self.onInit()
        self.show()

    def handleChanges(self):
        self.onChanges()
        self.show()

    def onChanges(self):
        pass

    def show(self):
        pass

    def onInit(self):
        pass

    def handleActionButtonOnPress(self, e):
        pass