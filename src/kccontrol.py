# Trade
from kucoin_futures.client import Trade


class KCT:
    def __init__(self, apiKey,  apiSecret, apiPassphrase):
        self.client = Trade(key=apiKey, secret=apiSecret, passphrase=apiPassphrase)

    def CreateLimit(self, symbol, side, leverage, amount, price):
        #size = sell or buy
        return self.client.create_limit_order(symbol, side, leverage, amount, price)["orderId"]

    def CancelOrderByID(self, orderID):
        return self.client.cancel_order(orderID)

    def CancelAllOrderSymbol(self, symbol):
        return self.client.cancel_all_limit_order(symbol)

#Market
from kucoin_futures.client import Market
import pandas as pd


class KCM:
    def __init__(self):
        self.client = Market(url='https://api-futures.kucoin.com')

    def GetKlineData(self, symbol, min):
        #min = Minutes
        raw = self.client.get_kline_data(symbol, min)
        df = {
            'date':[],
            'open':[],
            'high':[],
            'low':[],
            'close':[],
            'volume':[],
        }
        for r in raw:
            df['date'].append(pd.to_datetime(r[0], utc=True, unit='ms'))
            df['open'].append(r[1])
            df['high'].append(r[2])
            df['low'].append(r[3])
            df['close'].append(r[4])
            df['volume'].append(r[5])
        df = pd.DataFrame(df)
        return df

    def GetTickSize(self, symbol):
        return self.client.get_contract_detail(symbol)["tickSize"]

    def GetCurrentPrice(self, symbol):
        raw = self.client.get_kline_data(symbol, 1)
        return raw[-1][4]