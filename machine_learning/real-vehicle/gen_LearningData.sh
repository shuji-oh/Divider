#!/bin/sh

echo "mean,stdev,variance,skew,kurtosis,max,rms,en,label\n" > delay_time.csv
python3 raw2delay.py delay_262.txt | sed 's/\ /,/g' | sed 's/$/,ECU0/' | grep -v \^0.0000,0.0000, | head -n 360 >> delay_time.csv 
python3 raw2delay.py delay_610.txt | sed 's/\ /,/g' | sed 's/$/,ECU1/' | grep -v \^0.0000,0.0000, | head -n 360 >> delay_time.csv
python3 raw2delay.py delay_025.txt | sed 's/\ /,/g' | sed 's/$/,ECU2/' | grep -v \^0.0000,0.0000, | head -n 360 >> delay_time.csv
python3 raw2delay.py delay_0b4.txt | sed 's/\ /,/g' | sed 's/$/,ECU3/' | grep -v \^0.0000,0.0000, | head -n 360 >> delay_time.csv
python3 raw2delay.py delay_127.txt | sed 's/\ /,/g' | sed 's/$/,ECU4/' | grep -v \^0.0000,0.0000, | head -n 360 >> delay_time.csv
python3 raw2delay.py delay_1c4.txt | sed 's/\ /,/g' | sed 's/$/,ECU5/' | grep -v \^0.0000,0.0000, | head -n 360 >> delay_time.csv
python3 raw2delay.py delay_154.txt | sed 's/\ /,/g' | sed 's/$/,ECU6/' | grep -v \^0.0000,0.0000, | head -n 360 >> delay_time.csv
