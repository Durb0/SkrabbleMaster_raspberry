from abc import ABC, abstractmethod

class Component(ABC):

    def __init__(self):
        self.onInit()
        self.show()

    def onInit(self):
        pass

    def handleActionButtonOnPress(self, e):
        pass

    def show(self):
        pass