#!/usr/bin/env python3
'''
    Author: GYZHENG
    Email: guanggyz@gmail.com
    Purpose: Retrieve the Wind speed/direction from Taiwan CWB
    Ref Url: http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467570&datepicker=2016-01-11
    Usgae: ./windCrawler.py --date 2016-01-11 --station 467570
'''
from html.parser import HTMLParser
import urllib.request,urllib.parse
import re
import sys
import json
import argparse
'''
備註:
0   => 觀測時間
1   => 測站氣壓
2   => 海平面氣壓
3   => 氣溫
4   => 露點溫度
5   => 相對溼度
6   => 風速
7   => 風向
8   => 最大陣
9   => 最大陣風風向
10  => 降水量
11  => 降水時數
12  => 日照時數
13  => 全天空日射量
14  => 能見度
註：T表微量，x表故障，V表風向不定，/表不明
'''
class WindHTMLParser(HTMLParser):
    def init(self):
        self.isTr = False
        self.isTd = False
        self.count = 0
        self.windSpeed = []
        self.windDirection = []
    #override
    def handle_starttag(self,tag,attrs):
        if tag == 'tr':
            self.isTr = True
            self.count = 0;
        elif tag == 'td':
            self.isTd = True

    def handle_data(self, data):
        #if not done and isTarget
        if self.isTr and self.isTd:
            data = data.strip()
            if self.count == 6:
                self.windSpeed.append(data)
            elif self.count ==7:
                self.windDirection.append(data)
            self.count = self.count + 1
        else:
            pass
    def handle_endtag(self,tag):
        if tag == 'tr':
            self.isTr = False
        elif tag == 'td':
            self.isTd = False
        pass
    def get_result_list(self):
        result = []
        for i in range(len(self.windSpeed)):
            #result.append({'t':i+1,'ws':self.windSpeed[i],'wd':self.windDirection[i]})
            result.append({'time':i+1,'wind':{'speed':self.windSpeed[i],'direction':self.windDirection[i]}})
        return result

class WindCrawler:
    def __init__(self,station,date):
        #default settings
        self.url_host = 'http://e-service.cwb.gov.tw'
        self.url_path = '/HistoryDataQuery/DayDataController.do?command=viewMain&station='+station+"&datepicker="+date
        self.result= []
    def start(self):
        try:
            url = self.url_host+self.url_path
            request = urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"})
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8','ignore')
            #print(content)
            parser = WindHTMLParser()
            parser.init()
            parser.feed(content)
            self.result = parser.get_result_list()
            #print(json.dumps(self.result))
        except Exception as e:
            print('exception:'+e)
            sys.exit(-1)
    def get_result(self):
        return self.result

if __name__ == '__main__':
    #Set up argument list
    ap = argparse.ArgumentParser(description='Retrieve daily wind speed and direction data from Taiwan CWB.')
    ap.add_argument('--station', help='Enter the station ID of the Location',nargs=1)
    ap.add_argument('--date', help='Example: 2015-12-01',nargs=1)
    args = ap.parse_args()
    #Set default value
    station = "467570" #新竹
    dateReg = re.compile('\d\d\d\d-\d\d-\d\d')
    if args.date != None and dateReg.match(''.join(args.date)) != None:
        date = ''.join(args.date)
    else:
        ap.print_help()
        sys.exit(-1)

    if args.station != None:
        station = ''.join(args.station)
    else:
        print("No station parameter detected, use 467570(HsinChu) as default")

    print('Station: '+station+'\r\nDate: '+date)
    wc = WindCrawler(station,date)
    wc.start()
    result = wc.get_result()
    if len(result) == 0:
        print("ERROR: No data!")
        sys.exit(-1)
    fileName = station+"_"+date+".json"
    with open(fileName, "w") as outfile:
        json.dump({'station':station,'date':date,'data':result}, outfile, indent=4)
    print('Finish! Please checkout file '+fileName)

