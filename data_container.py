import pandas as pd
import yfinance as yf

class data_collector():
    def __init__(self, ticker):
        self.ticker = ticker

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
    
    def calculate_TaxRate():
        '''
        Docstring for calculate_TaxRate
        Tax Rate = Tax provision/pretax income
        '''

    def calculate_NOPAT():
        '''
        Docstring for calculate_NOPAT
        NOPAT stands for Net Operating Profit After Tax
        NOPAT = EBIT x (1 - Tax rate)
        '''



aapl_data = data_collector("AAPL")
print(aapl_data)

apple = yf.Ticker('AAPL')
print(apple.info)
