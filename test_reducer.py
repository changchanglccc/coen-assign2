#!/usr/bin/python
"""A more advanced Reducer, using Python iterators and generators."""

import sys
import numpy as np

        #max,min,median,std
data_list =[]
key = None
pre_result =[]
mid_result =[]
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
    data_list.append(max(item[1]))
    data_list.append(min(item[1]))
    data_list.append(np.median(item[1]))
    data_list.append(np.std(item[1]))
    # print "result is :--------", result
    result.append(item[0])
    result.append(data_list)

    final_result.append(result)

    data_list = []
    result =[]
    # print "result is :--------", result
print final_result


