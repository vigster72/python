import csv

file2 = open(r"/home/netscout/Downloads/test.txt","w+")
with open('/home/netscout/Downloads/api-test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
          #  print(f'\t{row[0]} works in the {row[1]} department, and was born in.')
            file2.write("<ApplicationConfigurations>")
            file2.write("<application>" + {row[1]} + "</endport>")
            line_count += 1
    #print(f'Processed {line_count} lines.')