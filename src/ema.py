from stock_indicators import indicators
from stock_indicators.indicators.common.enums import CandlePart
from stock_indicators import Quote


def GetEma(df, length):
    quotes_list = [
            Quote(d,o,h,l,c,v) 
            for d,o,h,l,c,v 
            in zip(df['date'], df['open'], df['high'], df['low'], df['close'], df['volume'])
        ]
    emaPointHigh = indicators.get_ema(quotes_list, length, CandlePart.HIGH)[-1].ema
    emaPointLow = indicators.get_ema(quotes_list, length, CandlePart.LOW)[-1].ema
    return emaPointHigh, emaPointLow