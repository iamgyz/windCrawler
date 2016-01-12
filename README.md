# windCrawler
A wind speed/direction crawler for Central Weather Bureau  
http://e-service.cwb.gov.tw/HistoryDataQuery/

In this repository, we just get the wind speed and direction from the daily record data sets.  

### Installation:  
```
git clone https://github.com/iamgyz/windCrawler.git
```

### Environment:  
Test in Python3.4^

### Example:  
```
./windCrawler.py --date 2016-01-11 --station 467570  
```

### result:  
A JSON format output contains 01:00~24:00 total 24 wind speed(m/s)/direction(degree。) data sets
```json
{
    "date": "2016-01-11",
    "station": "467570",
    "data": [
        {
            "wind": {
                "speed": "2.3",
                "direction": "10.0"
            },
            "time": 1
        },
        {
            "wind": {
                "speed": "2.6",
                "direction": "30.0"
            },
            "time": 2
        },
        {
            "wind": {
                "speed": "1.7",
                "direction": "50.0"
            },
            "time": 3
        },
        {
            "wind": {
                "speed": "2.3",
                "direction": "70.0"
            },
            "time": 4
        },
        {
            "wind": {
                "speed": "1.8",
                "direction": "50.0"
            },
            "time": 5
        },
        {
            "wind": {
                "speed": "2.5",
                "direction": "10.0"
            },
            "time": 6
        },
        {
            "wind": {
                "speed": "0.3",
                "direction": "30.0"
            },
            "time": 7
        },
        {
            "wind": {
                "speed": "1.1",
                "direction": "80.0"
            },
            "time": 8
        },
        {
            "wind": {
                "speed": "2.4",
                "direction": "70.0"
            },
            "time": 9
        },
        {
            "wind": {
                "speed": "1.8",
                "direction": "50.0"
            },
            "time": 10
        },
        {
            "wind": {
                "speed": "0.6",
                "direction": "70.0"
            },
            "time": 11
        },
        {
            "wind": {
                "speed": "0.9",
                "direction": "10.0"
            },
            "time": 12
        },
        {
            "wind": {
                "speed": "1.4",
                "direction": "350.0"
            },
            "time": 13
        },
        {
            "wind": {
                "speed": "2.6",
                "direction": "360.0"
            },
            "time": 14
        },
        {
            "wind": {
                "speed": "2.0",
                "direction": "30.0"
            },
            "time": 15
        },
        {
            "wind": {
                "speed": "0.6",
                "direction": "30.0"
            },
            "time": 16
        },
        {
            "wind": {
                "speed": "0.5",
                "direction": "130.0"
            },
            "time": 17
        },
        {
            "wind": {
                "speed": "1.8",
                "direction": "110.0"
            },
            "time": 18
        },
        {
            "wind": {
                "speed": "1.7",
                "direction": "70.0"
            },
            "time": 19
        },
        {
            "wind": {
                "speed": "0.3",
                "direction": "60.0"
            },
            "time": 20
        },
        {
            "wind": {
                "speed": "0.1",
                "direction": "0.0"
            },
            "time": 21
        },
        {
            "wind": {
                "speed": "0.3",
                "direction": "60.0"
            },
            "time": 22
        },
        {
            "wind": {
                "speed": "2.0",
                "direction": "40.0"
            },
            "time": 23
        },
        {
            "wind": {
                "speed": "0.4",
                "direction": "30.0"
            },
            "time": 24
        }
    ]
}
```

### output:  
A JSON file with the filename `<stationID>_<date>.json`  

