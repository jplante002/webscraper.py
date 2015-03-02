#! usr/bin/env Python3

import urllib.request

def main():
    cbs = urllib.request.urlopen('http://www.cbsnews.com/latest/rss/main')
    info = str(cbs.read())

    for i in info:
        while i == '<link>':
            print(i)
            if i == '<\link>':
                break
            break

main()
