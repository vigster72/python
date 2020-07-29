import csv
import os
f1 = open('/home/netscout/Downloads/test.txt', "w")
# txt_file = '/home/netscout/Downloads/output.txt'
# my_output_file = " "
with open('/home/netscout/Downloads/api-test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    ServerIP = []
    Port = []
    #line_count = 0
    for row in readCSV:
        Port = row[1]
        ServerIP = row[0]
     #   while line_count == 0:
    while readCSV:
    #my_output_file = open(txt_file, "w")
         f1.write ("<ApplicationConfigurations>\n")
         f1.write ("<application>"+Port +"</endport>\n")
        #line_count +=1
       # else
    f1.close()