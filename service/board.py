from object.button import Button, LightButton
from object.button.buttonLogic import KeyBoardButtonLogic
from object.screen import Screen
from core.service import Service
from object.button.buttonLogic import RaspberryButtonLogic
from object.light.lightLogic import KeyBoardLightLogic, RaspberryLightLogic
import os


@Service
class Board:

    def __init__(self):
        #if os is raspberry, use raspberry button and light logic
        if os.uname()[4][:3] == 'arm':
            self.mode_button = LightButton(RaspberryButtonLogic(6), RaspberryLightLogic(5))
            self.action_button = Button(RaspberryButtonLogic(16, False))
        else:
            self.mode_button = LightButton(KeyBoardButtonLogic('m'), KeyBoardLightLogic('l'))
            self.action_button = Button(KeyBoardButtonLogic('a'))
        self.screen = Screen(240, 320)
        self.camera = None  # TODO créer la classe Camera
