import time

class Config:
    def __init__(self):
        # How much standard currency the bot will start with the make trades
        self.userWalletStandard = None
        # The type of standard currency the bot will trade with
        # Default is USD
        self.currencyStandard = None
        # How much cryptp currency the bot will start with the make trades
        self.userWalletCrypto = None
        # The type of crypto currency the bot will trade with
        # Default is XBT
        self.currencyCrypto = None
        # Where the bot will be getting its trade data from. Only BitMEX and CoinMarketCap
        self.dataSource = None
        # How long the bot will wait (in seconds) for better prices when one side is hit
        # Default is 1800 seconds (30 minutes)
        self.waitTime = None
        # How much spread the bot will take when making trades.
        # Value is a decimal between 1 and 0, 1 for max aggression, 0 for none
        # Default is 0.5
        # NOTE: Higher aggression will result in higher short-term profits, but quickly drain the market
        self.aggressiveness = None
        # How long the bot will run before termination sequence begins
        # Value is current time + a number of seconds
        # Default is 86400 seconds (one day)
        self.terminateTime = None
        # In the case that, during shutdown procedure, the bot is unable to offload all sell offers,
        # should the bot chance quicker shutdown at a loss of money
        self.lossyShutdown = None

    def setConfigs(self, textfile):
        params = open(textfile, "r").read().split('/')
        self.userWalletStandard = float(params[3])
        self.currencyStandard = params[5]
        self.userWalletCrypto = float(params[7])
        self.currencyCrypto = params[9]
        self.dataSource = params[11]
        self.waitTime = float(params[13])
        self.aggressiveness = float(params[15])
        self.terminateTime = float(params[17]) + time.time()
        self.lossyShutdown = bool(params[19])