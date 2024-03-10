from .core import Component

class AnalyseComponent(Component):

    def __init__(self):
        super().__init__()

    def onSetContext(self):
        print('mode analyse')
        light = self.context.board.mode_button.setLight(False)
        assert not light

    def handleActionButtonOnPress(self, e):
        print('[A] action button pressed')

    def show(self):
        pass #TODO