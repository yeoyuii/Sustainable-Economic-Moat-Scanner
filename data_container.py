import pandas as pd
import yfinance as yf

class data_collector():
    def __init__(self, ticker: str):
        self.ticker = ticker
        stock = yf.Ticker(self.ticker)
        self.income_stmt = stock.get_income_stmt() 
        self.balance_sheet = stock.balance_sheet
        self.effective_tax_rate = 0
        self.info = stock.info
        self.avrg_ic = None
        self.calc_NOPAT = None
    
    def __repr__(self):
        return f"data collector: {self.ticker}"

    def data_collector(self) -> None:
        '''
        Retreiving stock information and returning selective data
        '''

        # Storing information into a dictionary
        data = {
            'Stock' : self.info.get('longName', self.ticker),
            'Price' : self.info.get('currentPrice', 0),
            'Market_cap' : self.info.get('marketCap', 0)
        }

        return data 
    
    def calculate_TaxRate(self) -> float:
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


    def calculate_NOPAT(self) -> float:
        '''
        Docstring for calculate_NOPAT
        NOPAT stands for Net Operating Profit After Tax
        NOPAT = EBIT x (1 - Tax rate)
        '''
        if self.effective_tax_rate == 0:
            self.calculate_TaxRate()
        getting_EBIT = self.income_stmt.loc['EBIT']
        calc_EBIT = self.income_stmt.loc['EBIT'].iloc[0]
        self.calc_NOPAT = calc_EBIT * (1 - self.effective_tax_rate)
        return self.calc_NOPAT

    def calculate_avrg_invested_cap(self) -> float:
        '''
        Docstring for calculate_avrg_invested_cap
        Returns Average Invested Capital as a float
        '''
        current_ic = self.calculate_Invested_Capital(period=0)
        previous_ic = self.calculate_Invested_Capital(period=1)
        self.avrg_ic = (current_ic + previous_ic) / 2
        return self.avrg_ic
    
    def calculate_ROIC(self) -> float:
        '''
        Docstring for calculate_ROIC
        Return on invested Capital (ROIC) = NOPAT / average invested capital
        '''
        return self.calc_NOPAT / self.avrg_ic



aapl_data = data_collector("AAPL")
print(aapl_data)


apple = yf.Ticker('AAPL')
print(apple.info)
print(aapl_data.calculate_NOPAT())
