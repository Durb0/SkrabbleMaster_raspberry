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

    def handleActionButtonOnPress(self, e):
        if e >= 2:
            self.long_choice.action()
        else:
            self.short_choice.action()

    def show(self): #TODO à adapter selon le periphérique d'affichage
        print(self.title)
        print(self.message)
        print('short:', self.short_choice.label)
        print('long:', self.long_choice.label)