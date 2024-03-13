from object.button import Button, LightButton
from object.button.buttonLogic import RaspberryButtonLogic
from core import Service
from object.light.lightLogic import KeyBoardLightLogic, RaspberryLightLogic


@Service
class Board:

    def __init__(self):
        self.mode_button = LightButton(RaspberryButtonLogic(6), KeyBoardLightLogic(5))
        self.action_button = Button(RaspberryButtonLogic(16, False))
        self.camera = None  # TODO créer la classe Camera
        self.screen = None  # TODO créer la classe Screen
