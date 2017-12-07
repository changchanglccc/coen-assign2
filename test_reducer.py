#!/usr/bin/python
"""A more advanced Reducer, using Python iterators and generators."""

import sys
import numpy as np


import logging
import logging.handlers

LOG_FILE = 'reducer.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)
fmt = '%(msecs)d - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)

logger = logging.getLogger('reducer')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


data_list =[]
key = None
pre_result =[]
mid_result =[]
result =[]
final_result=[]

key_data=[] #[key,[xx,xx]]

logger.info('first info message')
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

for item in mid_result:
    data_list.append(max(item[1]))
    data_list.append(min(item[1]))
    data_list.append(np.median(item[1]))
    data_list.append(np.std(item[1]))
    result.append(item[0])
    result.append(data_list)

    final_result.append(result)

    data_list = []
    result =[]
print final_result
logger.debug('first debug message')


