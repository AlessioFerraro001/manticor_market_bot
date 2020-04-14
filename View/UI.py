class UI:
    def __init__(self):
        self.internalBot = None

    def start(self):
        self.internalBot.start()

    def end(self):
        self.internalBot.terminate()
