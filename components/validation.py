from core.component import Component

class Choice:

    def __init__(self, label, action):
        self.label = label
        self.action = action

class ValidationComponent(Component):

    def __init__(self, title, message, short_choice: Choice, long_choice: Choice):
        self.title = title
        self.message = message
        self.short_choice = short_choice
        self.long_choice = long_choice
        super().__init__()

    def setTemplate(self):
        screen_mid_width = 120
        screen_mid_height = 160
        width = 200
        height = 160
        cursor = [
            screen_mid_width - width/2,
            screen_mid_height - height/2
        ]
        return [
            "rectangle_fill?color=0xFFFF;x_start={};y_start={};x_end={};y_end={};".format(cursor[0], cursor[1], width, height),
            "text?value={};color=0x0000;size=1;x_start={};y_start={};".format(self.title, cursor[0] + 10, cursor[1] + 10),
            "text?value={};color=0x0000;size=3;x_start={};y_start={};".format(self.message, cursor[0] + 10, cursor[1] + 30),
            "text?value={};color=0x0000;size=2;x_start={};y_start={};".format(self.short_choice.label, cursor[0] + 10, cursor[1] + 100),
            "text?value={};color=0x0000;size=2;x_start={};y_start={};".format(self.long_choice.label, cursor[0] + 10, cursor[1] + 130),
        ]

    def handleActionButtonOnPress(self, e):
        if e >= 2:
            self.long_choice.action()
        else:
            self.short_choice.action()