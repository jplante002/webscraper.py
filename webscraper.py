#! usr/bin/env Python3 

##import urllib.request
##
##def main():
##temp = ""
##sky = ""
##data = urllib.request.urlopen("http://dsx.weather.com/wxd/v2/(MORecord/en_US;NCRecord/en_US)/USNY1143:1:US?api=7bb1c920-7027-4289-9c96-ae5e263980bc&jsonp=angular.callbacks._6")
##js = str(data.read())
##pos = js.find('tmpF')
##for x in js[pos+6:pos+10]:
##    if x != ",":
##        temp += x
##    else:
##        break
##print ("Current Temperature:", temp)
##pos2 = js.find('"wx"')
##for i in js[pos2+6:pos2+13]:
##    if i != '"':
##        sky += i
##    else:
##        break
##print("Current Conditions:", sky)
##
##main()
#! usr/bin/env Python3

#comment
import urllib.request

def findNums(cords):
    nums = [0,1,2,3,4,5,6,7,8,9]
    resultList = []
    i = 0
    x = 0
    while i != 10:
        for x in range(len(cords)):
            if cords[x] == str(nums[i]):
                resultList.append(cords[x])
        i=i+1
        
    result = ''.join(resultList)
    return result

def day():
    dayOW = ""
    dayOWPos = js.find('dow"')
    for i in js[dayOWPos+6:dayOWPos+17]:
        if i != '"':
            dayOW += i
        else:
            break
    return dayOW

def main():
    #dayOW = ""
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
    lowTemp = js[lowTempPos:lowTempPos+9]

    #dayOWPos = js.find('dow"')
    #for i in js[dayOWPos+6:dayOWPos+17]:
     #   if i != '"':
      #      dayOW += i
       # else:
        #    break
        
    print("Temp:", findNums(tempCords), "degrees fahrenheit")
    print("Date:", date)
    print("Weather:", weather)
    print("Temp High:", findNums(highTemp))
    print("Temp Low:", findNums(lowTemp))
    print("Today is", day())
main()


