import csv
import os
import requests
import_file = '/home/netscout/Downloads/site-import.csv'
export_file = '/home/netscout/Downloads/site-api1.txt'
dummy_file = "/home/netscout/Downloads/site-api-input1.txt" # This file is what will used in the curl
user_name = 'jvigliotti'
user_pass = 'Bat#cave0220'
server_ip = '172.23.246.11'
server_port = '443'
file2 = open(export_file,"w") #Creates the Api import file
with open(import_file , 'r') as file:  # This csv data import to with Api
    reader = csv.reader(file,delimiter = ',',skipinitialspace=True)
    #This creating the xml for the SBA import
    for row in reader:
        file2.write("   " + "<site>" + "\n")
        file2.write("       " + "<addresses>"+"\n")
        file2.write("         " + "<address>"+row[0]+row[1]+"</address>"+"\n")
        file2.write("       " + "</addresses>"+ "\n")
        file2.write("       " + "<speedKbps>"+row[2]+"</speedKbps>"+"\n")
        file2.write("       " + "<name>"+row[3]+"</name>" + "\n")
        file2.write("   " + "</site>" + "\n")
    file.close()
    file2.close()
    # open original file in read mode and new file to write mode
    with open(export_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write begining parm to the new the file
        write_obj.write("<sites>" + '\n')
        # Read lines from original file one by one and append them to new file
        for line in read_obj:
            write_obj.write(line)
    # remove original api file
    os.remove(export_file)
    #Append to bottom of file
    with open(dummy_file, "a") as file_object:
        # Append closing of the parm at end of file
        file_object.write("</sites>" + "\n")
#run the curl process to import into nG1
