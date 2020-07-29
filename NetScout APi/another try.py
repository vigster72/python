import csv
file2 = open(r"/home/netscout/Downloads/test.txt","w")
with open('/home/netscout/Downloads/api-test.csv') as myFile:
    reader = csv.DictReader(myFile)
    ServerIP = []
    Port = []
    line_count = 0
    for row in reader:
        if line_count == 0:
         Port = row[1]
         ServerIP = row[0]
         file2.write("<ApplicationConfigurations>")
         file2.write("<application>" + Port + "</endport>")
         line_count += 1