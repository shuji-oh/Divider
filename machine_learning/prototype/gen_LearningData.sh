#!/bin/sh

echo "mean,stdev,variance,skew,kurtosis,max,min,rms,en,label\n" > delay_time.csv
python3 raw2delay.py delay_panda.txt | sed 's/\ /,/g' | sed 's/$/,ECU0/' | grep -v \^0.0000,0.0000, | tail -n 1000 >> delay_time.csv
python3 raw2delay.py delay_rpi.txt | sed 's/\ /,/g' | sed 's/$/,ECU1/' | grep -v \^0.0000,0.0000, |tail -n 1000 >> delay_time.csv
python3 raw2delay.py delay_arduino1.txt | sed 's/\ /,/g' | sed 's/$/,ECU2/' | grep -v \^0.0000,0.0000, | tail -n 1000 >> delay_time.csv
python3 raw2delay.py delay_arduino2.txt | sed 's/\ /,/g' | sed 's/$/,ECU3/' | grep -v \^0.0000,0.0000, | tail -n 1000 >> delay_time.csv
python3 raw2delay.py delay_suzuki_ecu.txt | sed 's/\ /,/g' | sed 's/$/,ECU4/' | grep -v \^0.0000,0.0000, | tail -n 1000 >> delay_time.csv
python3 raw2delay.py delay_toyota_meter.txt | sed 's/\ /,/g' | sed 's/$/,ECU5/' | grep -v \^0.0000,0.0000, | tail -n 1000 >> delay_time.csv
python3 raw2delay.py delay_suzuki_meter.txt | sed 's/\ /,/g' | sed 's/$/,ECU6/' | grep -v \^0.0000,0.0000, | tail -n 1000 >> delay_time.csv
