Divider: Delay-Time Based Sender Identification in Automotive Networks
====

## Overview

Divider is sender Identification method on CAN bus.

Shuji Ohira et al. "Divider: Delay-Time Based Sender Identification in Automotive Networks"

```
@inproceedings{ohira2020Divider,
  title={Divider: Delay-Time Based Sender Identification in Automotive Networks},
  author={Ohira, Shuji and Kibrom Desta, Araya and Arai, Ismail and Kitagawa, Tomoya and Fujikawa, Kazutoshi},
  booktitle={IEEE Compsac Workshop},
  pages={1--8},
  year={2020},
  organization={IEEE}
}
```

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
Quartus (Quartus Prime 17.0)  

## Usage (machine learning)

$ git clone https://github.com/ohirangosta/Divider  
$ cd machine_learning/prototype  
$ python3 knn.py  

## Author

[shuji-oh](https://github.com/shuji-oh)
