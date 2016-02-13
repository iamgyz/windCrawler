#!/bin/sh
station=467490
year=2015
month=12
for i in {1..31}
do
    if [ $i -lt 10 ]
    then
        i='0'$i
    fi
    ./windCrawler.py --station $station --date $year-$month-$i
done
echo "Done!"
