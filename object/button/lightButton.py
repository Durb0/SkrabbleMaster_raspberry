from object.button.button import Button


class LightButton(Button):
    def __init__(self, button_logic, light_logic):
        super().__init__(button_logic)
        self.light_logic = light_logic

    def switchLight(self):
        self.light_logic.switch()
        return self.light_logic.isOn()

    def isLight(self):
        return self.light_logic.isOn()

    def setLight(self, light_status):
        self.light_logic.setOn(light_status)
        return self.light_logic.isOn()


if __name__ == '__main__':
    def testHandlePress(button):
        button.switchLight()
        print("light on" if button.isLight() else "light off")

    from object.button.buttonLogic import KeyBoardButtonLogic
    button = LightButton(KeyBoardButtonLogic())
    button.on_press.connect(lambda e: testHandlePress(button))
    input('Press enter to exit')
    print('Exiting')

