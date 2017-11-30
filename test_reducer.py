#!/usr/bin/python
"""A more advanced Reducer, using Python iterators and generators."""

import sys
import numpy as np

mid_result = []         #max,min,median,std
data_list =[]
key = None
pre_result =[]
result =[]
final_result=[]

key_data=[] #[key,[xx,xx]]

for line in sys.stdin:
    # line = line.strip()
    data = line.strip().split('\t')

    if data[0] != key:
        pre_result=[]
        key_data=[]
        pre_result.append(data[0])
        key_data.append(float(data[1]))
        pre_result.append(key_data)
        mid_result.append(pre_result)
        key = data[0]
    else:
        key_data.append(float(data[1]))
    # print "pre_ ",pre_result
# print "mid_result is ",mid_result           #need change to min max...

for item in mid_result:
    # print type(item[1])
    result.append(max(item[1]))
    result.append(min(item[1]))
    result.append(np.median(item[1]))
    result.append(np.std(item[1]))
    # print "result is :--------", result
    final_result.append(item[0])
    final_result.append(result)
    result = []
    # print "result is :--------", result
print final_result


