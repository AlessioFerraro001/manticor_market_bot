import time

class Order:
    def __init__(self, isBuy):
        self.timePlaced = time.time()
        self.isBuy = isBuy