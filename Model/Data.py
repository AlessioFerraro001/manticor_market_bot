from Model import Order

class Data:
    def __init__(self, config):
        # The given config data
        self.config = config
        # The current highest price to buy cryptocurrency
        self.bestBid = self.updateBid(config.dataSource)
        # The current lowest price to sell cryptocurrency
        self.bestAsk = self.updateAsk(config.dataSource)
        # The id of the most recent order
        self.orderID = 0
        # The list of all our active orders with the time they were sent and if they were buy or sell
        self.pastOrders = []
        # The amount of standard currency we have to buy with
        self.standardAmount = self.config.userWalletStandard
        # The amount of cryptocurrency we have to sell
        self.cryptoAmount = self.config.userWalletCrypto
        # The number of buy orders we have completed by now
        self.numBuy = 0
        # The number of sell orders we have completed so far
        self.numSell = 0

    def updateBid(self, source):
        #placeholder
        self.bestBid = 100
        return self.bestBid

    def updateAsk(self, source):
        #placeholder
        self.bestAsk = 100
        return self.bestAsk

    def addOrder(self, isBuy):
        self.pastOrders.append(Order(isBuy))
        self.orderID += 1

    def deleteOrder(self, id):
        self.pastOrders.pop(id)
        self.orderID -= 1