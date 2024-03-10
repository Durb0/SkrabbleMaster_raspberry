from board import Board
from enum import Enum
from turn import Turn
from typing import List
import keyboard
from components import Component, AnalyseComponent, PartyComponent, ValidationComponent

class SkrabbleMaster:

    def __init__(self, component: Component = AnalyseComponent()):
        self.board: Board = Board()
        self.set_component(component)
        self.turns:List[Turn] = []

        self.board.mode_button.on_press.connect(self.handleModeButtonOnPress)
        self.board.action_button.on_press.connect(self.handleActionButtonOnPress)

        keyboard.on_press_key('l', lambda e: print(self.board.mode_button.isLight())) #TEMP à supprimer lorsqu'on aura un bouton lumineux fonctionnel

    def set_component(self, component:Component):
        self.component = component
        self.component.context = self

    def handleActionButtonOnPress(self, duration):
        self.component.handleActionButtonOnPress(duration)


    def cleanCache(self):
        self.turns = []
        print('cache cleaned')

    def handleModeButtonOnPress(self, e):
        if e >= 2:
            self.cleanCache()
        else:
            if self.component.__class__ == AnalyseComponent:
                self.set_component(PartyComponent())
            else:
                self.set_component(AnalyseComponent())




if __name__ == '__main__':
    sm = SkrabbleMaster()
    input('Press enter to exit')
    print('Exiting')