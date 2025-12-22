import pandas as pd
import yfinance as yf

def data_collector(ticker):
    '''
    Retreiving stock information and returning selective data
    '''
    stock = yf.Ticker(ticker)
    info = stock.info

    # Storing information into a dictionary
    data = {
        'Stock' : info.get('longName', ticker),
        'Price' : info.get('currentPrice', 0),
        'Market_cap' : info.get('marketCap', 0)
    }

    return data 

aapl_data = data_collector("AAPL")
print(aapl_data)

apple = yf.Ticker('AAPL')
print(apple.info)
