#! usr/bin/env Python3

import urllib.request
import threading
from time import gmtime, strftime
import sqlite3

DATABASE = 'stocks.db'

def getPrice():
    url = urllib.request.urlopen('http://finance.yahoo.com/q?s=aapl')
    js = str(url.read()) #Puts the webpage in a string
    price = js.find('id="yfs_l84_aapl">') #Finds stock ticker
    priceCords = js[price+18:price+24] #Gets just the price
    return priceCords

def startLoop():
    t = threading.Timer(5, main).start() #Runs main() every 5 seconds

def dataBase(price, time):
    date = strftime("%b %d, %Y", gmtime())
    con = sqlite3.connect(DATABASE) #Open DB
    cur = con.cursor()
    #cur.execute("""CREATE TABLE apple (price, time, date)""")
    #Adds the price and time to the database
    cur.execute("insert into apple values (?,?,?)",(price,time,date))
    con.commit()
    for row in cur.execute('SELECT * FROM apple ORDER BY date, time'):
        print(row) #Prints each entry in the database
    con.close()

def main():
    time = strftime("%H:%M:%S", gmtime()) #Gets time
    price = getPrice()
    dataBase(price, time) #Writes to the database
    
    #print("Apple's current stock price is", price, "at", time)
    #startLoop()
main()
