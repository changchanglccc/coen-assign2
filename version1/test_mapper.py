#!/usr/bin/python
"""A more advanced Mapper, using Python iterators and generators."""

# import csv
#
# def read_csv():
#     key_value_list =[]
#     flag = 0
#     with open('nms.csv') as csvfile:
#         readCSV = csv.reader(csvfile,delimiter = ",")
#         for row in readCSV:
#             if flag > 0:
#                 key_value_list.append(map(row))
#             flag = flag + 1
#     return key_value_list
#
# def map(list):
#     mylist = []
#     pre_key = list[0]+list[2]
#     key = pre_key[:-6]      # use locationyear as key
#     mylist.append(key)
#     mylist.append(list[7])  #list[1] is the value
#     return mylist
#
# def main(separator='\t'):
#     for key_value in read_csv():
#         print '%s\t%s' % (key_value[0],key_value[1])
#
# if __name__ == "__main__":
#     main()

import sys

def read_input(file):
    key_value_list = []
    flag = 0
    for line in file:
        # split the line into words
        data = line.split(',')
        # print "data: ", data
        if flag > 0:
            key_value_list.append(map(data))
        flag = flag + 1
    yield key_value_list

def map(list):
    mylist = []
    pre_key = list[0]+list[2]
    key = pre_key[:-6]      # use locationyear as key
    mylist.append(key)
    mylist.append(list[7])  #list[1] is the value
    return mylist


def main(separator='\t'):
    # list =read_input(sys.stdin)
    for key_value in read_input(sys.stdin):
        for item in key_value:
            print '%s\t%s' % (item[0], item[1])

if __name__ == "__main__":
    main()