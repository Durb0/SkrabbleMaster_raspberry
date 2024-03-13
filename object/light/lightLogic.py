from abc import ABC, abstractmethod
from gpiozero import LED


class LightLogic(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @abstractmethod
    def switch(self):
        pass

    @abstractmethod
    def isOn(self):
        pass

    @abstractmethod
    def setOn(self, on):
        pass


class KeyBoardLightLogic(LightLogic):
    def __init__(self, on=False):
        self._on = on

    def on(self):
        self._on = True
        print("Light on")

    def off(self):
        self._on = False
        print("Light off")

    def switch(self):
        self._on = not self._on
        print(f'Light {"on" if self._on else "off"}')

    def isOn(self):
        return self._on

    def setOn(self, on):
        self._on = on
        (self.on if self._on else self.off)()


class RaspberryLightLogic(LightLogic):
    def __init__(self, pin, on=False):
        self.led = LED(pin, initial_value=on)

    def on(self):
        self.led.on()

    def off(self):
        self.led.off()

    def switch(self):
        self.led.toggle()

    def isOn(self):
        return self.led.is_lit

    def setOn(self, on):
        self.led.value = 1 if on else 0
        (self.on if on else self.off)()
