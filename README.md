# Divider
====

## Overview

Divider is attacks detection method on CAN bus.

Shuji Ohira et al. "Divider: Delay-time based on Various ECU Identification and Attacker Detection in Controller Area Network"

## Description



## Directory Structure

Divider  
┣━ hardware  
┃	┣━ main.v  
┃	┣━ fifo.v  
┃	┣━ spi.v  
┃	┣━ out_hex.v  
┃	┣━ measure_time.v  
┃	┗━ run.sh  
┣━ machine_learning  
┃	┣━ prototype  
┃   ┃   ┣━ knn.py  
┃   ┃   ┣━ raw2delay.py  
┃   ┃   ┣━ gen_LearningData.sh  
┃	┃   ┗━ delay_time.py  
┃	┗━ real-vehicle  
┃       ┣━ knn.py  
┃       ┣━ raw2delay.py  
┃       ┣━ gen_LearningData.sh  
┃	    ┗━ delay_time.csv  
┣━ spi_recv.c  
┗━ paper.pdf  

## Requirement

python3
gcc
Quartus (Quartus Prime 17.0)

## Usage (machine learning)

$ git clone https://github.com/ohirangosta/Divider  
$ cd machine_learning/prototype  
$ python3 knn.py  

## Contribution

## Author

[rangosta](https://github.com/ohirangosta)
