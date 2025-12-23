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

def calc_COGS(ticker):
    '''
    Calculating cost of goods
    formula: COGS = beginning inventory + purchases in current period - ending inventory
    '''
    beginning_inv = ticker.info.get('sharesOutstanding')
    cost_of_goods = beginning_inv + curr_purchase_period - ending_inv

def calculate_netRev():
    '''
    Docstring for calculate_rev
    Net Revenue = Gross Revenue - Returns - Discounts - Sales Allowances
    '''

def forecast_rev():
    '''
    Docstring for forecast_rev
    revenue = price x quantity
    '''

def calculate_gross_profit():
    '''
    Docstring for gross proft
    Gross Profit = Net Revenue - Cost of Goods Sold (COGS)
    '''

def calculate_EBIT():
    '''
    Docstring for EBIT
    EBIT stands for “Earnings Before Interest and Taxes”
    EBIT = gross profit - operating expenses
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
