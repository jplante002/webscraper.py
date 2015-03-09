#! usr/bin/env python3

import urllib.request

def stopRead(title):
    i = 0
    read=[]
    while title[i] != '<':
        read.append(title[i])
        i+=1
        
    result = ''.join(read)
    return result
    
#def links():

def main():
    cbs = urllib.request.urlopen('http://www.cbsnews.com/latest/rss/main')
    info = str(cbs.read())
    
    
    pos = info.find('/news/')
    story1 = info[pos+6:pos+100]
    

    print("the top story is", stopRead(story1))

main()
