import csv
from itertools import groupby
from operator import itemgetter


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

def map(list):
    mylist = []
    key = []
    key.append(list[0])    #use a tuple as key
    key.append(list[2])
    mylist.append(key)
    mylist.append(list[7])  #list[1] is the value
    return mylist

def main(separator='\t'):

    # print read_csv()

    for key_value in read_csv():

        # print key_value

        for key, value in groupby(key_value, itemgetter(0)):
            try:
                total_count = sum(int(count) for current_word, count in value)
                print "%s%s%d" % (key, separator, total_count)
            except ValueError:
                # count was not a number, so silently discard this item
                pass

            # print key


if __name__ == "__main__":
    main()
