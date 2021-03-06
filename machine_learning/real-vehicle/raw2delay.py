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
count_r = 0
with open(params[1],'r') as f:
    for row in f:
        if count_r > 10000:
            break
        if '[packet_' == row[0:8]:
            if count > 2:
                print('{:.4f}'.format(mean(sum_delay_list)),'{:.4f}'.format(stdev(sum_delay_list)),'{:.4f}'.format(variance(sum_delay_list)),'{:.4f}'.format(skew(sum_delay_list)),'{:.4f}'.format(kurtosis(sum_delay_list)),'{:.4f}'.format(max(sum_delay_list)),'{:.4f}'.format(rms(sum_delay_list)),'{:.4f}'.format(en(sum_delay_list)))
                count_r += 1
            sum_delay_list.clear()
            count = 0
        else :
            row_spt = row.split(',')
            row_id_spt = row_spt[0].split(':')
            row_time_spt = row_spt[1].split(':')
            elapsed_time = int(row_time_spt[1], 16) * 20
            ideal_time = int((elapsed_time+500)/2000)*2000
            delay_time = elapsed_time - ideal_time
            sum_delay_list.append(delay_time)
            count += 1
