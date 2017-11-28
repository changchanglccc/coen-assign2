# import csv
#
# with open('nms.csv') as csvfile:
#     readCSV = csv.reader(csvfile,delimiter = ",")
#     flag = 0
#     for row in readCSV:
#         if flag > 0:
#             print(row)
#             print '------'
#             print(row[0])
#             print '------'
#             print(row[0],row[1],row[2])
#             print '===================='
#         flag = flag + 1
#
#

from numpy import median,std
import sys
# list1=[-10,-5,0,5,10]
#
# print min(list1)
# print max(list1)
# print median(list1)
# print std(list1)


# def read_input(file):
#     flag = 0
#     for line in file:
#         if flag > 0:
#             # split the line into words
#             yield line.rstrip().split(',')
#         flag = flag + 1
#
# data = read_input(sys.stdin)
# print type(data)

def map(list):
    mylist = []
    key = []
    key.append(list[0])    #use a list as key
    key.append(list[2])
    mylist.append(key)
    mylist.append(list[7])  #list[1] is the value
    return mylist

list1 = [0,1,2,3,4,5,6,7]
list2 = [10,11,12,13,14,15,16,17]
test_list =[]

test_list.append(map(list1))
test_list.append(map(list2))
print map(list1)
print
print test_list

