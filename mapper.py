#!/usr/bin/python
"""A more advanced Mapper, using Python iterators and generators."""

import sys
import csv

# input from csv file:
def read_csv():
    key_value_list =[]
    flag = 0
    with open('nms.csv') as csvfile:
        readCSV = csv.reader(csvfile,delimiter = ",")
        for row in readCSV:
            if flag > 0:
                key_value_list.append(map(row))
                # print(row[0], row[2], row[7])
                # print '-----------------------'
            flag = flag + 1
    return key_value_list


# def read_input(file):
#     key_value_list =[]      #list of list
#     flag = 0
#     for line in file:
#         if flag > 0:
#             # split the line into words
#             yield line.rstrip().split(',')
#             key_value_list.append(map(line))
#         flag = flag + 1


def map(list):
    mylist = []
    key = []
    key.append(list[0])    #use a tuple as key
    key.append(list[2])
    mylist.append(key)
    mylist.append(list[7])  #list[1] is the value
    return mylist


def main(separator='\t'):
    # input comes from STDIN (standard input)

    # data = read_input(sys.stdin)        #data is a list?

    print read_csv()

    for key_value in read_csv():
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1

        # for word in words:
        #     print '%s%s%d' % (word, separator, 1)

        print key_value

if __name__ == "__main__":
    main()


# Question: key,value 's definition place;
#      the list: to use numpy function






# #!/usr/bin/python
# import sys
#
# # input comes from STDIN (standard input)
# for line in sys.stdin:
#     # remove leading and trailing whitespace
#     line = line.strip()
#     # split the line into words
#     words = line.split()
#     # increase counters
#     for word in words:
#         # write the results to STDOUT (standard output);
#         # what we output here will be the input for the
#         # Reduce step, i.e. the input for reducer.py
#         #
#         # tab-delimited; the trivial word count is 1
#         print '%s\t%s' % (word, 1)


# def read_csv():
#     # input from csv file:
#     with open('nms.csv') as csvfile:
#         readCSV = csv.reader(csvfile, delimiter=",")
#         for row in readCSV:
#             # print(row)
#             # print '-----'
#             print(row[0],row[2],row[7])
#             print '===================='