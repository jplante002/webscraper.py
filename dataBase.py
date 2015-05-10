#! usr/bin/env Python3

import sqlite3
from graphics import *

DATABASE = 'testStocks.db'
con = sqlite3.connect(DATABASE) #Open DB
cur = con.cursor()

def dataList():
    #Adds all the data into an array
    stockList = []
    i = 0
    for row in cur.execute('SELECT * FROM stockName ORDER BY price'): #puts every row into an array
        stockList.append(row)
        i += 1
    return stockList

def sortLowest(stockList):
    stockList.reverse() #reverses the list so it is low to high
    lowestRows = stockList[0:10] #first 10 of the prices
    lowestTimes = []
    for i in range(len(lowestRows)):
        pos = str(lowestRows[i]).find("""'""") #finds the position where the price starts
        lowestTimes.append(str(lowestRows[i])[pos+1:pos+6]) #Adds the price to the list
    lowestTimes.sort() #sorts highest to lowest
    startTime = lowestTimes[0] #Gets the first price in list
    endTime = lowestTimes[-1] #Gets the last price in list
    return startTime, endTime

def sortHighest(stockList):
    topTen = []
    stockList.reverse()
    topRows = stockList[0:10] #Top 10 rows
    #print(topRows)
    for a in range(len(topRows)):
        str(topRows[a])
    
    topTimes = []
    for i in range(len(topRows)):
        pos = str(topRows[i]).find("""'""")
        topTimes.append(str(topRows[i])[pos+1:pos+6])
    topTimes.sort()
    startTime = topTimes[0]
    endTime = topTimes[-1]
    return startTime, endTime

def printAll():
    listDates = []
    a = 0
    i = 0
    for row in cur.execute("""SELECT * FROM stockName ORDER BY date, time"""): #ASC = Lowest && DESC = Highest
        listDates.append(str(row[0]))
        i+=1

    return listDates[:40]

def createTable():
    cur.execute("""CREATE TABLE stockName (price, time, date)""")

def drawTable(listdates):
    win = GraphWin("Stock Graph", 1200, 800)
    title = Text(Point(600, 100), 'Stock Price Graph')
    title.draw(win)
    xAxis = Line(Point(1050,700), Point(200,700))
    yAxis = Line(Point(200,700), Point(200, 200))
    xAxis.draw(win)
    yAxis.draw(win)
    x = 220
    m = 700
    for p in range(120):
        if (p%10) == 0:
            text = Text(Point(180,m), str(p))
            text.draw(win)
            m = m - 25

    for e in range(8):
        hour = ['9:30','10:30','11:30','12:30','1:30','2:30','3:30','4:00']
        text = Text(Point(x,750), str(hour[e]))
        text.draw(win)
        x = x + 112
        
    x = 220
    for i in range(len(listdates)): #Plots the prices
        height= int(listdates[i])
        point = Circle(Point(x, (height*5)), 5)
        point.setFill('black')
        point.draw(win)
        x = x + 20
    
def main():
    listdates = printAll()
    drawTable(listdates)
    datalist = dataList()
    print('\nDone')
main()
































    

##    createTable()
##
##    cur.execute("insert into stockName values (?,?,?)", (90, '9:30', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (91, '9:40', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (90, '9:50', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (89, '10:00', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (93, '10:10', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (94, '10:20', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '10:30', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (91, '10:40', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '10:50', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '11:00', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '11:10', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (90, '11:20', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (88, '11:30', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (90, '11:40', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (91, '11:50', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (93, '12:00', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (94, '12:10', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (94, '12:20', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (93, '12:30', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (96, '12:40', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (97, '12:50', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (98, '13:00', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (97, '13:10', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (98, '13:20', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (98, '13:30', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (98, '13:40', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (100, '13:50', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (99, '14:00', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (99, '14:10', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (97, '14:20', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (98, '14:30', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (97, '14:40', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (90, '14:50', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (89, '15:00', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (93, '15:10', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (94, '15:20', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '15:30', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (91, '15:40', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '15:50', 'April, 27'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '16:00', 'April, 27'))
##
##    cur.execute("insert into stockName values (?,?,?)", (90, '9:30', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (91, '9:40', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (90, '9:50', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (89, '10:00', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (93, '10:10', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (94, '10:20', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '10:30', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (91, '10:40', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '10:50', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '11:00', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '11:10', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (90, '11:20', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (88, '11:30', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (90, '11:40', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (91, '11:50', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (93, '12:00', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (94, '12:10', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (94, '12:20', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (93, '12:30', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (96, '12:40', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (97, '12:50', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (98, '13:00', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (97, '13:10', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (98, '13:20', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (98, '13:30', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (98, '13:40', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (100, '13:50', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (99, '14:00', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (99, '14:10', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (97, '14:20', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (98, '14:30', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (97, '14:40', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (90, '14:50', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (89, '15:00', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (93, '15:10', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (94, '15:20', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '15:30', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (91, '15:40', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '15:50', 'April, 28'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '16:00', 'April, 28'))
##
##    cur.execute("insert into stockName values (?,?,?)", (90, '9:30', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (91, '9:40', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (90, '9:50', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (89, '10:00', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (93, '10:10', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (94, '10:20', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '10:30', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (91, '10:40', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '10:50', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '11:00', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '11:10', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (90, '11:20', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (88, '11:30', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (90, '11:40', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (91, '11:50', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (93, '12:00', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (94, '12:10', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (94, '12:20', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (93, '12:30', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (96, '12:40', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (97, '12:50', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (98, '13:00', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (97, '13:10', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (98, '13:20', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (98, '13:30', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (98, '13:40', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (100, '13:50', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (99, '14:00', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (99, '14:10', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (97, '14:20', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (98, '14:30', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (97, '14:40', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (90, '14:50', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (89, '15:00', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (93, '15:10', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (94, '15:20', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '15:30', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (91, '15:40', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '15:50', 'April, 29'))
##    cur.execute("insert into stockName values (?,?,?)", (92, '16:00', 'April, 29'))
##    con.commit()
