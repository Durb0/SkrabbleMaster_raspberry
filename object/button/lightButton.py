from object.button.button import Button

class LightButton(Button):

    def __init__(self,logic, light_status = False):
        super().__init__(logic)
        self.light_status = light_status

    def switchLight(self):
        self.light_status = not self.light_status
        return self.light_status

    def isLight(self):
        return self.light_status

    def setLight(self, light_status):
        self.light_status = light_status
        return self.light_status


if __name__ == '__main__':

    def testHandlePress(button):
        button.switchLight()
        print("light on" if button.isLight() else "light off")

    from object.button.buttonLogic import KeyBoardButtonLogic
    button = LightButton(KeyBoardButtonLogic())
    button.on_press.connect(lambda e: testHandlePress(button))
    input('Press enter to exit')
    print('Exiting')

