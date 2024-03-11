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
    def __init__(self, pin, pull_up=True, threshold=1):
        self._button = Button(pin, pull_up=pull_up)
        self._threshold = threshold

    def initEvents(self, on_press_method, on_release_method):
        self._button.wait_for_press()
        begin = time.time()
        self._button.wait_for_release()
        press_duration = time.time() - begin

        if press_duration < self._threshold:
            on_press_method()
        else:
            on_release_method()
