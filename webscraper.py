#! usr/bin/env Python3

import urllib.request

def findNums(cords):
    nums = ["-","0","1","2","3","4","5","6","7","8","9"]
    resultList = []
    i = 0
    x = 0
    while i != len(nums):
        for x in range(len(cords)):
            if cords[x] == nums[i]:
                resultList.append(cords[x])
        i=i+1

    result = ''.join(resultList)
    return result

def findWord(dayPOS): #Extracts the word
    dayOW = []
    i = 0
    while dayPOS[i] != '"': #Adds the characters until "
        dayOW.append(dayPOS[i])
        i += 1

    result = ''.join(dayOW)
    return result

def main():
    url = urllib.request.urlopen('http://dsx.weather.com/%28wxd/v2/BERecord/en_US;wxd/v2/MORecord/en_US;x/v2/web/WebDFRecord/en_US%29/USNY1143:1:US?api=7bb1c920-7027-4289-9c96-ae5e263980bc&jsonp=angular.callbacks._8')
    js = str(url.read())

    tempPos = js.find('tmpF')
    tempCords = js[tempPos:tempPos+9]

    datePos = js.find('_procTmLocal')
    date = js[datePos+15:datePos+25]

    weatherPos = js.find('wx"')
    weather = js[weatherPos+5:weatherPos+18]

    highTempPos = js.find('hiTmpF":')
    highTemp = js[highTempPos:highTempPos+10]

    lowTempPos = js.find('loTmpF":')
    lowTemp = js[lowTempPos:lowTempPos+10]

    dayOWPos = js.find('dow"')
    dayOW = js[dayOWPos+6:dayOWPos+18]

    print("Temp:", findNums(tempCords), "degrees fahrenheit")
    print("Weather:", findWord(weather))
    print("High:", findNums(highTemp), "F")
    print("Low:", findNums(lowTemp), "F")
    print("Today is", findWord(dayOW))
    print("Date:", date)
main()



