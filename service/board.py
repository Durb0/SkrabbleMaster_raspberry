from object.button import Button, LightButton
from object.button.buttonLogic import KeyBoardButtonLogic
from object.screen import Screen
from core.service import Service
from object.button.buttonLogic import RaspberryButtonLogic
from object.light.lightLogic import KeyBoardLightLogic, RaspberryLightLogic


@Service
class Board:

    def __init__(self):
        self.screen = Screen(240, 320)
        self.mode_button = LightButton(RaspberryButtonLogic(6), RaspberryLightLogic(5))
        self.action_button = Button(RaspberryButtonLogic(16, False))
        self.camera = None  # TODO créer la classe Camera
