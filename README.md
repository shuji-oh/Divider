Divider: Delay-Time Based Sender Identification in Automotive Networks
====

## Overview

Divider is sender Identification method based on delay caused by CAN transceiver.

[Shuji Ohira, Araya Kibrom Desta, Tomoya Kitagawa, Ismail Arai, Kazutoshi Fujikawa, "Divider: Delay-Time Based Sender Identification in Automotive Networks," 2020 IEEE 44th Annual Computer Software and Applications Conference (COMPSAC), pp.1490-1497, July. 2020.](https://arxiv.org/pdf/2008.10941.pdf)

```
@inproceedings{ohira2020Divider,
  title={Divider: Delay-Time Based Sender Identification in Automotive Networks},
  author={Ohira, Shuji and Kibrom Desta, Araya and Kitagawa, Tomoya and Arai, Ismail and Fujikawa, Kazutoshi},
  booktitle={IEEE 44th Annual Computer Software and Applications Conference (COMPSAC)},
  pages={1490--1497},
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

$ git clone https://github.com/shuji-oh/Divider  
$ cd machine_learning/prototype  
$ python3 knn.py  

## Author

[shuji-oh](https://github.com/shuji-oh)
