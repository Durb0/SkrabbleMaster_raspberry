from PySignal import Signal
import time
from .buttonLogic import ButtonLogic
from typing import Annotated

class Button:

    def __init__(self, buttonLogic:ButtonLogic):
        """
        Un bouton est un objet qui peut être pressé et relâché. Il a deux signaux, on_press et in_press.
        :param buttonLogic:
        """
        self.on_press: Signal = Signal() # Signal émis lorsque le bouton est relâché
        self.in_press: Signal = Signal() # Signal émis lorsque le bouton est pressé
        self.logic = buttonLogic
        self.is_pressed = False
        self.t0 = 0
        self.logic.initEvents(self.handle_press, self.handle_release)

    def handle_press(self, e):
        if not self.is_pressed:
            self.is_pressed = True
            self.t0 = time.time()
        else:
            self.in_press.emit(time.time() - self.t0)

    def handle_release(self, e):
        self.on_press.emit(time.time() - self.t0)
        self.is_pressed = False
        self.t0 = 0


if __name__ == '__main__':
    from components.button.buttonLogic import KeyBoardButtonLogic
    button = Button(KeyBoardButtonLogic())
    button.on_press.connect(lambda e: print('Button pressed for', e, 'seconds'))
    button.in_press.connect(lambda e: print('Button is pressed for', e, 'seconds'))
    input('Press enter to exit')
    print('Exiting')