import csv

with open('nms.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter = ",")
    for row in readCSV:
        print(row)
        print '------'
        print(row[0])
        print '------'
        print(row[0],row[2],row[2])
        print '===================='