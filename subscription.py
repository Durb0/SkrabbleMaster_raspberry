class Subscription:
    def __init__(self, listener, action):
        self.listener = listener
        self.action = action
        self.listener.connect(self.action)

    def disconnect(self):
        self.listener.disconnect(self.action)