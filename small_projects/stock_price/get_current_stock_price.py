import pandas as pds
import yfinance as yf
import argparse
import sys


from pathlib import Path

current_dir = Path(__file__).absolute().parent


def get_stock_price(stock_name):
    msft = yf.Ticker(stock_name)
    return msft.info.get('currentPrice', msft.info.get('regularMarketPrice', None))


def read_spreadsheet(file_name):
    file = (str(Path(current_dir, f'{file_name}.xlsx')))
    new_data = pds.read_excel(file)
    return new_data


def create_new_spreadsheet(file_name):
    lst_latest_price, lst_style_indicator, lst_profit_percentage, lst_profit, new_data = get_stock_details(file_name)
        
    new_data['LatestPrice'] = lst_latest_price
    new_data['PercentGain'] = lst_profit_percentage
    new_data['Gain'] = lst_profit
    new_data['StyleIndicator'] = lst_style_indicator
    
    new_data.style.apply(highlight_cells)
    new_data = new_data.sort_values(by='StockCode', ascending=False)
    # new_data.style.applymap(lambda val: 'green' if val=='green' else '')

    new_data.to_excel(f'{current_dir}/{file_name}_with_current_price.xlsx')

def get_stock_details(file_name):
    lst_latest_price = list()
    lst_style_indicator = list()
    lst_profit_percentage = list()
    lst_profit = list()
    dct_entered = dict()
    new_data = read_spreadsheet(file_name)

    for _, row in new_data.iterrows():
        print("Row", row.StockCode)
        actual_price = dct_entered.get(row.StockCode) or get_stock_price(row.StockCode)
        dct_entered[row.StockCode] = actual_price
        total_profit = actual_price - row.BuyPrice
        profit_percent = (total_profit/row.BuyPrice)*100
        my_profit = (row.Total * profit_percent)/100
        
        
        if actual_price >= row.TargetPrice:
            style_indicator = 'green'
        elif row.TargetPrice-actual_price <= 5:
            style_indicator = 'yellow'
        else:
            style_indicator = ''
        
        lst_style_indicator.append(style_indicator)
        lst_latest_price.append(actual_price)
        lst_profit.append(my_profit)
        lst_profit_percentage.append(profit_percent)
    return lst_latest_price,lst_style_indicator,lst_profit_percentage,lst_profit,new_data

def highlight_greaterthan_1(s):
        # lst1 = ['']*4
        # print("inside this styling function", s.StyleIndicator)
        # lst1.append(f'background-color: {s.StyleIndicator}')
        return ['background-color: green']
    
def highlight_cells():
    # provide your criteria for highlighting the cells here
    return ['background-color: yellow']


def client_runner(args):
    parser = argparse.ArgumentParser(description='Target Price')
    parser.add_argument('--excel_file_name', '-f', default='ShareSheet', help='enter the excel file name')
    parsed_args = parser.parse_args(args)
    return parsed_args

if __name__ == '__main__':
    util_args = sys.argv[1:]
    parsed_args = client_runner(util_args)
    
    print(parsed_args.excel_file_name)
    create_new_spreadsheet(parsed_args.excel_file_name)