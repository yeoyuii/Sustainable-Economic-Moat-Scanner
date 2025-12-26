import pandas as pd
import yfinance as yf

class data_collector():
    def __init__(self, ticker):
        self.ticker = ticker
        self.income_stmt = self.ticker.get_income_stmt()
        self.effective_tax_rate = 0

    def data_collector(self, ticker):
        '''
        Retreiving stock information and returning selective data
        '''
        stock = yf.Ticker(self.ticker)
        info = stock.info

        # Storing information into a dictionary
        data = {
            'Stock' : info.get('longName', ticker),
            'Price' : info.get('currentPrice', 0),
            'Market_cap' : info.get('marketCap', 0)
        }

        return data 
    
    def calculate_TaxRate(self):
        '''
        Docstring for calculate_TaxRate
        Tax Rate = Tax provision/pretax income
        '''

        operating_income = self.income_stmt.loc['OperatingIncome']

        # iloc[0] = Most recent period (TTM for annual, latest quarter for quarterly)
        most_recent_op_income = operating_income.iloc[0]
        tax_expense = self.income_stmt.loc['TaxProvision'].iloc[0]
        pretax_income = self.income_stmt.loc['PretaxIncome'].iloc[0]

        self.effective_tax_rate = tax_expense / pretax_income

        return self.effective_tax_rate


    def calculate_NOPAT(self):
        '''
        Docstring for calculate_NOPAT
        NOPAT stands for Net Operating Profit After Tax
        NOPAT = EBIT x (1 - Tax rate)
        '''
        getting_EBIT = self.income_stmt.loc['EBIT']
        calc_EBIT = self.income_stmt.loc['EBIT'].iloc[0]
        calc_NOPAT = calc_EBIT * (1 - self.effective_tax_rate)
        return calc_NOPAT



aapl_data = data_collector("AAPL")
print(aapl_data)

apple = yf.Ticker('AAPL')
print(apple.info)
