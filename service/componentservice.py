from core import Service, Component
from PySignal import Signal

from .board import Board
from core import inject, Service

@Service
@inject('_board',Board)
class ComponentService:

    def __init__(self):
        self._component = None
        self.component_changed = Signal()

        self._board.action_button.on_press.connect(self.handleActionButtonOnPress)


    def handleActionButtonOnPress(self, duration):
        if self._component:
            self._component.handleActionButtonOnPress(duration)
        else:
            print('No component found')


    def setComponent(self, component:Component):
        self._component = component
        self.component_changed.emit()

    def getComponent(self):
        return self._component