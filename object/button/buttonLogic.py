import time
from abc import ABC, abstractmethod
import keyboard
from gpiozero import Button


class ButtonLogic(ABC):

    @abstractmethod
    def initEvents(self, on_press_method, on_release_method):
        pass


class KeyBoardButtonLogic(ButtonLogic):

    def __init__(self, key = 'k'):
        self.key = key

    def initEvents(self, handle_press_method, handle_release_method):
        keyboard.on_press_key(self.key, handle_press_method)
        keyboard.on_release_key(self.key, handle_release_method)


class RaspberryButtonLogic(ButtonLogic):
    def __init__(self, pin, pull_up=True):
        self._button = Button(pin, pull_up=pull_up)

    def initEvents(self, on_press_method, on_release_method):
        self._button.when_pressed = on_press_method
        self._button.when_released = on_release_method
