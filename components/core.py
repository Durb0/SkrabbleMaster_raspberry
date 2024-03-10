from abc import ABC, abstractmethod

class Component(ABC):

    def __init__(self):
        self._context = None

    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context):
        self._context = context
        self.onSetContext()

    def onSetContext(self):
        pass

    def handleActionButtonOnPress(self, e):
        pass

    @abstractmethod
    def show(self):
        pass