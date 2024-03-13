from object.button import Button, LightButton
from object.button.buttonLogic import KeyBoardButtonLogic
from object.screen import Screen
from core.service import Service

@Service
class Board:

    def __init__(self):
        self.mode_button = LightButton(KeyBoardButtonLogic('m'))
        self.action_button = Button(KeyBoardButtonLogic('a'))
        self.camera = None #TODO créer la classe Camera
        self.screen = Screen(240, 320)


if __name__ == '__main__':
    board = Board()
    board.mode_button.on_press.connect(lambda e: print('Mode button pressed'))
    board.action_button.on_press.connect(lambda e: print('Action button pressed'))
    input('Press enter to exit')
    print('Exiting')
