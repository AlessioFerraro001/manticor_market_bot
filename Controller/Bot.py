import time


class Bot:
    def __init__(self, data):
        self.didSomethingHappen = False
        self.didTerminate = False
        self.config = data.config
        self.data = data

    def terminate(self):
        self.didTerminate = True

    def start(self):
        print("Termination time: %f" % self.config.terminateTime)
        while not self.didTerminate:
            print("Trades are occuring!")
            print("Current time: %f" % time.time())
            print("Best Ask: %f / Best Bid: %f" % (self.data.bestAsk, self.data.bestBid))
            if self.config.terminateTime <= time.time():
                self.didTerminate = True
                print("Trades have concluded!")
            else:
                print("-------Waiting 10 secs-------")
                time.sleep(10)
