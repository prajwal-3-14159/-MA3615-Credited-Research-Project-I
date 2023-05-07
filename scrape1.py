import requests
import csv
import os
from bs4 import BeautifulSoup

stock_symbols = ['HDFCBANK', 'ICICIBANK', 'KOTAKBANK', 'AXISBANK', 'INDUSINDBK', 'BANKBARODA', 'BANKINDIA', 'IDBI', 'IDFCFIRSTB', 'PNB', 'RBLBANK', 'SBIN', 'YESBANK', 'CANBK', 'FEDERALBNK']

#Skipped ['BANDHANBNK']
#list stock symbols with indexes start from 0
stock_symbols = list(enumerate(stock_symbols, start=0))

ratio_urls = ['https://www.moneycontrol.com/financials/hdfcbank/ratiosVI/HDF01', 'https://www.moneycontrol.com/financials/icicibank/ratiosVI/ICI02#ICI02', 'https://www.moneycontrol.com/financials/kotakmahindrabank/ratiosVI/KMB', 'https://www.moneycontrol.com/financials/axisbank/ratiosVI/AB16', 'https://www.moneycontrol.com/financials/indusindbank/ratiosVI/IIB', 'https://www.moneycontrol.com/financials/bankofbaroda/ratiosVI/BOB', 'https://www.moneycontrol.com/financials/bankindia/ratiosVI/BOI', 'https://www.moneycontrol.com/financials/idbibank/ratiosVI/IDB05', 'https://www.moneycontrol.com/financials/idfcfirstbank/ratiosVI/IDF01', 'https://www.moneycontrol.com/financials/punjabnationalbank/ratiosVI/PNB05', 'https://www.moneycontrol.com/financials/rblbank/ratiosVI/RB03', 'https://www.moneycontrol.com/financials/statebankindia/ratiosVI/SBI', 'https://www.moneycontrol.com/financials/yesbank/ratiosVI/YB#YB', 'https://www.moneycontrol.com/financials/bandhanbank/ratiosVI/BB09#BB09', 'https://www.moneycontrol.com/financials/canarabank/ratiosVI/CB06', 'https://www.moneycontrol.com/financials/federalbank/ratiosVI/FB']

balancesheet_urls = ['https://www.moneycontrol.com/financials/hdfcbank/balance-sheetVI/HDF01/1#HDF01', 'https://www.moneycontrol.com/financials/icicibank/balance-sheetVI/ICI02%23ICI02', 'https://www.moneycontrol.com/financials/kotakmahindrabank/balance-sheetVI/KMB#KMB', 'https://www.moneycontrol.com/financials/axisbank/balance-sheetVI/AB16#AB16', 'https://www.moneycontrol.com/financials/indusindbank/balance-sheetVI/IIB#IIB', 'https://www.moneycontrol.com/financials/bankofbaroda/balance-sheetVI/BOB#BOB', 'https://www.moneycontrol.com/financials/bankofindia/balance-sheetVI/BOI#BOI', 'https://www.moneycontrol.com/financials/idbibank/balance-sheetVI/IDB05#IDB05', 'https://www.moneycontrol.com/financials/idfcfirstbank/balance-sheetVI/IDF01#IDF01', 'https://www.moneycontrol.com/financials/punjabnationalbank/balance-sheetVI/PNB05#PNB05', 'https://www.moneycontrol.com/financials/rblbank/balance-sheetVI/RB03#RB03', 'https://www.moneycontrol.com/financials/statebankindia/balance-sheetVI/SBI#SBI', 'https://www.moneycontrol.com/financials/yesbank/balance-sheetVI/YB#YB', 'https://www.moneycontrol.com/financials/bandhanbank/balance-sheetVI/BB09#BB09', 'https://www.moneycontrol.com/financials/canarabank/balance-sheetVI/CB06#CB06', 'https://www.moneycontrol.com/financials/federalbank/balance-sheetVI/FB#FB']

pnl_urls = ['https://www.moneycontrol.com/financials/hdfcbank/profit-lossVI/HDF01#HDF01', 'https://www.moneycontrol.com/financials/icicibank/profit-lossVI/ICI02#ICI02', 'https://www.moneycontrol.com/financials/kotakmahindrabank/profit-lossVI/KMB#KMB', 'https://www.moneycontrol.com/financials/axisbank/profit-lossVI/AB16#AB16', 'https://www.moneycontrol.com/financials/indusindbank/profit-lossVI/IIB#IIB', 'https://www.moneycontrol.com/financials/bankofbaroda/profit-lossVI/BOB#BOB', 'https://www.moneycontrol.com/financials/bankofindia/profit-lossVI/BOI#BOI', 'https://www.moneycontrol.com/financials/idbibank/profit-lossVI/IDB05#IDB05', 'https://www.moneycontrol.com/financials/idfcfirstbank/profit-lossVI/IDF01#IDF01', 'https://www.moneycontrol.com/financials/punjabnationalbank/profit-lossVI/PNB05#PNB05', 'https://www.moneycontrol.com/financials/rblbank/profit-lossVI/RB03#RB03', 'https://www.moneycontrol.com/financials/statebankindia/profit-lossVI/SBI#SBI', 'https://www.moneycontrol.com/financials/yesbank/profit-lossVI/YB#YB', 'https://www.moneycontrol.com/financials/bandhanbank/profit-lossVI/BB09#BB09', 'https://www.moneycontrol.com/financials/canarabank/profit-lossVI/CB06#CB06', 'https://www.moneycontrol.com/financials/federalbank/profit-lossVI/FB#FB']

yearly_results_urls = ['https://www.moneycontrol.com/financials/hdfcbank/results/yearly/HDF01#HDF01', 'https://www.moneycontrol.com/financials/icicibank/results/yearly/ICI02#ICI02', 'https://www.moneycontrol.com/financials/kotakmahindrabank/results/yearly/KMB#KMB', 'https://www.moneycontrol.com/financials/axisbank/results/yearly/AB16#AB16', 'https://www.moneycontrol.com/financials/indusindbank/results/yearly/IIB#IIB', 'https://www.moneycontrol.com/financials/bankofbaroda/results/yearly/BOB#BOB', 'https://www.moneycontrol.com/financials/bankofindia/results/yearly/BOI#BOI', 'https://www.moneycontrol.com/financials/idbibank/results/yearly/IDB05#IDB05', 'https://www.moneycontrol.com/financials/idfcfirstbank/results/yearly/IDF01#IDF01', 'https://www.moneycontrol.com/financials/punjabnationalbank/results/yearly/PNB05#PNB05', 'https://www.moneycontrol.com/financials/rblbank/results/yearly/RB03#RB03', 'https://www.moneycontrol.com/financials/statebankindia/results/yearly/SBI#SBI', 'https://www.moneycontrol.com/financials/yesbank/results/yearly/YB#YB', 'https://www.moneycontrol.com/financials/bandhanbank/results/yearly/BB09#BB09', 'https://www.moneycontrol.com/financials/canarabank/results/yearly/CB06#CB06', 'https://www.moneycontrol.com/financials/federalbank/results/yearly/FB#FB']

#create a new folder called 'financials version 1' inside the current directory
dir = os.path.dirname(os.path.abspath(__file__))
dir = dir + '/' + "financials version 1"

#Create version one financial csv files in new folder called 'financials version 1'
for stock in stock_symbols:
    index = stock[0]
    stock_name = stock[1]
    
    filename = os.path.join(dir + '/' + stock_name + '.csv')
    csv_writer = csv.writer(open(filename, 'w'))

    pnl_url = pnl_urls[index]
    yearly_results_url = yearly_results_urls[index]
    ratio_url = ratio_urls[index]
    balancesheet_url = balancesheet_urls[index]

    #Get pnl data
    r = requests.get(pnl_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table', {'class': 'mctable1'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        csv_writer.writerow(cols)
    
    #Get yearly results data
    r = requests.get(yearly_results_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table', {'class': 'mctable1'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        csv_writer.writerow(cols)

    #Get ratio data
    r = requests.get(ratio_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table', {'class': 'mctable1'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        csv_writer.writerow(cols)

    #Get balance sheet data
    r = requests.get(balancesheet_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table', {'class': 'mctable1'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        csv_writer.writerow(cols)
    

