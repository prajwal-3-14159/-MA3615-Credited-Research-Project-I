import requests
import csv
import os
from bs4 import BeautifulSoup

stock_symbols = ['HDFCBANK', 'ICICIBANK', 'KOTAKBANK', 'AXISBANK', 'INDUSINDBK', 'BANKBARODA', 'BANKINDIA', 'IDBI', 'IDFCFIRSTB', 'PNB', 'RBLBANK', 'SBIN', 'YESBANK', 'CANBK', 'FEDERALBNK']

#Skipped ['BANDHANBNK']
#list stock symbols with indexes start from 0
stock_symbols = list(enumerate(stock_symbols, start=0))

ratio_urls_2 = ['https://www.moneycontrol.com/financials/hdfcbank/ratiosVI/HDF01/2#HDF01', 'https://www.moneycontrol.com/financials/icicibank/ratiosVI/ICI02/2#ICI02', 'https://www.moneycontrol.com/financials/kotakmahindrabank/ratiosVI/KMB/2#KMB', 'https://www.moneycontrol.com/financials/axisbank/ratiosVI/AB16/2#AB16', 'https://www.moneycontrol.com/financials/indusindbank/ratiosVI/IIB/2#IIB', 'https://www.moneycontrol.com/financials/bankofbaroda/ratiosVI/BOB/2#BOB', 'https://www.moneycontrol.com/financials/bankofindia/ratiosVI/BOI/2#BOI', 'https://www.moneycontrol.com/financials/idbibank/ratiosVI/IDB05/2#IDB05', 'https://www.moneycontrol.com/financials/idfcfirstbank/ratiosVI/IDF01/2#IDF01', 'https://www.moneycontrol.com/financials/punjabnationalbank/ratiosVI/PNB05/2#PNB05', 'https://www.moneycontrol.com/financials/rblbank/ratiosVI/RB03/2#RB03', 'https://www.moneycontrol.com/financials/statebankindia/ratiosVI/SBI/2#SBI', 'https://www.moneycontrol.com/financials/yesbank/ratiosVI/YB/2#YB', 'https://www.moneycontrol.com/financials/bandhanbank/ratiosVI/BB09/2#BB09', 'https://www.moneycontrol.com/financials/canarabank/ratiosVI/CB06/2#CB06', 'https://www.moneycontrol.com/financials/federalbank/ratiosVI/FB/2#FB']

balancesheet_urls_2 = ['https://www.moneycontrol.com/financials/hdfcbank/balance-sheetVI/HDF01/2#HDF01', 'https://www.moneycontrol.com/financials/icicibank/balance-sheetVI/ICI02/2#ICI02', 'https://www.moneycontrol.com/financials/kotakmahindrabank/balance-sheetVI/KMB/2#KMB', 'https://www.moneycontrol.com/financials/axisbank/balance-sheetVI/AB16/2#AB16', 'https://www.moneycontrol.com/financials/indusindbank/balance-sheetVI/IIB/2#IIB', 'https://www.moneycontrol.com/financials/bankofbaroda/balance-sheetVI/BOB/2#BOB', 'https://www.moneycontrol.com/financials/bankofindia/balance-sheetVI/BOI/2#BOI', 'https://www.moneycontrol.com/financials/idbibank/balance-sheetVI/IDB05/2#IDB05', 'https://www.moneycontrol.com/financials/idfcfirstbank/balance-sheetVI/IDF01/2#IDF01', 'https://www.moneycontrol.com/financials/punjabnationalbank/balance-sheetVI/PNB05/2#PNB05', 'https://www.moneycontrol.com/financials/rblbank/balance-sheetVI/RB03/2#RB03', 'https://www.moneycontrol.com/financials/statebankindia/balance-sheetVI/SBI/2#SBI', 'https://www.moneycontrol.com/financials/yesbank/balance-sheetVI/YB/2#YB', 'https://www.moneycontrol.com/financials/bandhanbank/balance-sheetVI/BB09/2#BB09', 'https://www.moneycontrol.com/financials/canarabank/balance-sheetVI/CB06/2#CB06', 'https://www.moneycontrol.com/financials/federalbank/balance-sheetVI/FB/2#FB']

pnl_urls_2 = ['https://www.moneycontrol.com/financials/hdfcbank/profit-lossVI/HDF01/2#HDF01', 'https://www.moneycontrol.com/financials/icicibank/profit-lossVI/ICI02/2#ICI02', 'https://www.moneycontrol.com/financials/kotakmahindrabank/profit-lossVI/KMB/2#KMB', 'https://www.moneycontrol.com/financials/axisbank/profit-lossVI/AB16/2#AB16', 'https://www.moneycontrol.com/financials/indusindbank/profit-lossVI/IIB/2#IIB', 'https://www.moneycontrol.com/financials/bankofbaroda/profit-lossVI/BOB/2#BOB', 'https://www.moneycontrol.com/financials/bankofindia/profit-lossVI/BOI/2#BOI', 'https://www.moneycontrol.com/financials/idbibank/profit-lossVI/IDB05/2#IDB05', 'https://www.moneycontrol.com/financials/idfcfirstbank/profit-lossVI/IDF01/2#IDF01', 'https://www.moneycontrol.com/financials/punjabnationalbank/profit-lossVI/PNB05/2#PNB05', 'https://www.moneycontrol.com/financials/rblbank/profit-lossVI/RB03/2#RB03', 'https://www.moneycontrol.com/financials/statebankindia/profit-lossVI/SBI/2#SBI', 'https://www.moneycontrol.com/financials/yesbank/profit-lossVI/YB/2#YB', 'https://www.moneycontrol.com/financials/bandhanbank/profit-lossVI/BB09/2#BB09', 'https://www.moneycontrol.com/financials/canarabank/profit-lossVI/CB06/2#CB06', 'https://www.moneycontrol.com/financials/federalbank/profit-lossVI/FB/2#FB']

yearly_results_urls_2 = ['https://www.moneycontrol.com/financials/hdfcbank/results/yearly/HDF01/2#HDF01', 'https://www.moneycontrol.com/financials/icicibank/results/yearly/ICI02/2#ICI02', 'https://www.moneycontrol.com/financials/kotakmahindrabank/results/yearly/KMB/2#KMB', 'https://www.moneycontrol.com/financials/axisbank/results/yearly/AB16/2#AB16', 'https://www.moneycontrol.com/financials/indusindbank/results/yearly/IIB/2#IIB', 'https://www.moneycontrol.com/financials/bankofbaroda/results/yearly/BOB/2#BOB', 'https://www.moneycontrol.com/financials/bankofindia/results/yearly/BOI/2#BOI', 'https://www.moneycontrol.com/financials/idbibank/results/yearly/IDB05/2#IDB05', 'https://www.moneycontrol.com/financials/idfcfirstbank/results/yearly/IDF01/2#IDF01', 'https://www.moneycontrol.com/financials/punjabnationalbank/results/yearly/PNB05/2#PNB05', 'https://www.moneycontrol.com/financials/rblbank/results/yearly/RB03/2#RB03', 'https://www.moneycontrol.com/financials/statebankindia/results/yearly/SBI/2#SBI', 'https://www.moneycontrol.com/financials/yesbank/results/yearly/YB/2#YB', 'https://www.moneycontrol.com/financials/bandhanbank/results/yearly/BB09/2#BB09', 'https://www.moneycontrol.com/financials/canarabank/results/yearly/CB06/2#CB06', 'https://www.moneycontrol.com/financials/federalbank/results/yearly/FB/2#FB']

dir = os.path.dirname(os.path.abspath(__file__))
dir = dir + '/' + "Financials"

for stock in stock_symbols:
    index = stock[0]
    stock_name = stock[1]
    
    filename = os.path.join(dir + '/' + stock_name + '.csv')
    csv_writer = csv.writer(open(filename, 'w'))

    dir2 = os.path.dirname(os.path.abspath(__file__))
    dir2 = dir2 + '/' + "Financials version 1"

    pnl_url = pnl_urls_2[index]
    balancesheet_url = balancesheet_urls_2[index]
    yearly_results_url = yearly_results_urls_2[index]
    ratio_url = ratio_urls_2[index]

    #get pnl data
    r = requests.get(pnl_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('table', attrs = {'class':'mctable1'})
    rows = table.find_all('tr')

    for row in rows:
        filename2 = os.path.join(dir2 + '/' + stock_name + '.csv')
        csv_reader = csv.reader(open(filename2, 'r'))

        for row2 in csv_reader:
            if(len(row2) > 0):
                if(row2[0] == row.find_all('td')[0].text):
                    cols = row.find_all('td')
                    cols = [ele.text.strip() for ele in cols]
                    cols.pop(0)
                    csv_writer.writerow(row2 + cols)
                    break
        
    #get balance sheet data
    r = requests.get(balancesheet_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('table', attrs = {'class':'mctable1'})
    rows = table.find_all('tr')

    for row in rows:
        filename2 = os.path.join(dir2 + '/' + stock_name + '.csv')
        csv_reader = csv.reader(open(filename2, 'r'))

        for row2 in csv_reader:
            if(len(row2) > 0):
                if(row2[0] == row.find_all('td')[0].text):
                    cols = row.find_all('td')
                    cols = [ele.text.strip() for ele in cols]
                    cols.pop(0)
                    csv_writer.writerow(row2 + cols)
                    break
    
    #get yearly results data
    r = requests.get(yearly_results_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('table', attrs = {'class':'mctable1'})
    rows = table.find_all('tr')

    for row in rows:
        filename2 = os.path.join(dir2 + '/' + stock_name + '.csv')
        csv_reader = csv.reader(open(filename2, 'r'))

        for row2 in csv_reader:
            if(len(row2) > 0):
                if(row2[0] == row.find_all('td')[0].text):
                    cols = row.find_all('td')
                    cols = [ele.text.strip() for ele in cols]
                    cols.pop(0)
                    csv_writer.writerow(row2 + cols)
                    break
    
    #get ratio data
    r = requests.get(ratio_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('table', attrs = {'class':'mctable1'})
    rows = table.find_all('tr')

    for row in rows:
        filename2 = os.path.join(dir2 + '/' + stock_name + '.csv')
        csv_reader = csv.reader(open(filename2, 'r'))

        for row2 in csv_reader:
            if(len(row2) > 0):
                if(row2[0] == row.find_all('td')[0].text):
                    cols = row.find_all('td')
                    cols = [ele.text.strip() for ele in cols]
                    cols.pop(0)
                    csv_writer.writerow(row2 + cols)
                    break
    

