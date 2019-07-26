import sys
from statistics import mean, median, variance, stdev
from scipy.stats import skew, kurtosis
from functools import reduce
from math import sqrt

def rms(xs):
    return sqrt(reduce(lambda a, x: a + x * x, xs, 0) / len(xs))

def en(xs):
    return reduce(lambda a, x: a + x * x, xs, 0) / len(xs)

params = sys.argv
sum_delay_list = []
count = 0
#with open('panda.dat','r') as f:
#with open('minato.dat','r') as f:
#with open('ard1.dat','r') as f:
#with open('ard2.dat','r') as f:
#with open('suzuki_ecu.dat','r') as f:
#with open('prius_meter.dat','r') as f:
with open(params[1],'r') as f:
    for row in f:
    	if '[Packet_' == row[0:8]:
            if count > 6:
                #print('{:.4f}'.format(mean(sum_delay_list)),'{:.4f}'.format(stdev(sum_delay_list)))
                #print('{:.4f}'.format(mean(sum_delay_list)),'{:.4f}'.format(stdev(sum_delay_list)),'{:.4f}'.format(variance(sum_delay_list)),'{:.4f}'.format(skew(sum_delay_list)),'{:.4f}'.format(kurtosis(sum_delay_list)),'{:.4f}'.format(max(sum_delay_list)),'{:.4f}'.format(rms(sum_delay_list)),'{:.4f}'.format(en(sum_delay_list)))
                print('{:.4f}'.format(mean(sum_delay_list)),'{:.4f}'.format(stdev(sum_delay_list)),'{:.4f}'.format(variance(sum_delay_list)),'{:.4f}'.format(skew(sum_delay_list)),'{:.4f}'.format(kurtosis(sum_delay_list)),'{:.4f}'.format(max(sum_delay_list)),'{:.4f}'.format(min(sum_delay_list)),'{:.4f}'.format(rms(sum_delay_list)),'{:.4f}'.format(en(sum_delay_list)))
                #print(mean(sum_delay_list),stdev(sum_delay_list),sum_delay_list)
            sum_delay_list.clear()
            count = 0
    	else :
            elapsed_time = int(row, 16) * 20
            ideal_time = int((elapsed_time+500)/2000)*2000
            delay_time = elapsed_time - ideal_time
            sum_delay_list.append(delay_time)
            count += 1
