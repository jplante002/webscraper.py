#! usr/bin/env Python3

import urllib.request
import threading
from time import gmtime, strftime
import sqlite3
from datetime import datetime

DATABASE = 'stocks.db'
con = sqlite3.connect(DATABASE) #Open DB
cur = con.cursor()

def getPrice():
    url = urllib.request.urlopen('http://finance.yahoo.com/q?s=aapl')
    js = str(url.read()) #Puts the webpage in a string
    price = js.find('id="yfs_l84_aapl">') #Finds stock ticker
    priceCords = js[price+18:price+24] #Gets just the price
    return priceCords

def loop():
    t = threading.Timer(60, main).start() #Runs main() every 5 seconds

def makeTable(name):
    cur.execute("""CREATE TABLE ? (price, time, date)""", name)

def dataBase(price, time):
    date = strftime("%b %d, %Y", gmtime())
    #Adds the price and time to the database
    
    cur.execute("insert into apple values (?,?,?)",(price, time, date))
    con.commit()
    for row in cur.execute('SELECT * FROM apple ORDER BY date, time'):
        #print(row) #Prints each entry in the database
        last = row
    return row

def printAll():
    for row in cur.execute('SELECT * FROM apple ORDER BY price, time'):
        print(row)

def main():
    time = datetime.now().strftime("%H:%M.%S") #Gets time 9:30.30
##    if("09:30.00" < time < "16:00.00"): #Stock market closes at 4pm
##        loop()
    price = getPrice()
    printAll()
    #print(dataBase(price, time)) #Writes to the database
main()
