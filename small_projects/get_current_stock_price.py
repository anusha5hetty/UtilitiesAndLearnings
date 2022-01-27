import pandas as pds
import yfinance as yf


def get_stock_price(stock_name):
    msft = yf.Ticker(stock_name)
    print(msft.info['currentPrice'])
    return msft.info['currentPrice']


def read_spreadsheet():
    file = ('C:/Users/ashetty/Documents/Personal_Git/OtherWorkspace/WorkSpace/small_projects/ShareSheet.xlsx')
    new_data = pds.read_excel(file)
    return new_data


def create_new_spreadsheet():
    lst_latest_price = list()
    lst_style_indicator = list()
    new_data = read_spreadsheet()

    for _, row in new_data.iterrows():
        print("Row", row.StockCode)
        actual_price = get_stock_price(row.StockCode)
        
        if actual_price >= row.TargetPrice:
            style_indicator = 'green'
        elif row.TargetPrice-actual_price <= 5:
            style_indicator = 'yellow'
        else:
            style_indicator = ''
        
        lst_style_indicator.append(style_indicator)
        lst_latest_price.append(actual_price)
        
    new_data['LatestPrice'] = lst_latest_price
    new_data['StyleIndicator'] = lst_style_indicator
    
    new_data.style.apply(highlight_cells)
    # new_data.style.applymap(lambda val: 'green' if val=='green' else '')

    new_data.to_excel('C:/Users/ashetty/Documents/Personal_Git/OtherWorkspace/WorkSpace/small_projects/NewFile.xlsx')

def highlight_greaterthan_1(s):
        # lst1 = ['']*4
        # print("inside this styling function", s.StyleIndicator)
        # lst1.append(f'background-color: {s.StyleIndicator}')
        return ['background-color: green']
    
def highlight_cells():
    # provide your criteria for highlighting the cells here
    return ['background-color: yellow']
   
create_new_spreadsheet()