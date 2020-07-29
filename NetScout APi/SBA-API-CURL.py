import csv
import os
import requests

import_file = '/home/netscout/Downloads/app-import.csv'
export_file = '/home/netscout/Downloads/app-api.txt'
dummy_file = "/home/netscout/Downloads/app-api-input.txt" # This file is what will used in the curl
filepath = '/home/netscout/Downloads/curl.sh' # Reserved for use later
file2 = open(export_file,"w") #Creates the Api import file
with open(import_file , 'r') as file:  # This csv data import to with Api
    reader = csv.reader(file,delimiter = ',',skipinitialspace=True)
    #This creating the xml for the SBA import
    for row in reader:
        file2.write("   "+"<ApplicationConfiguration>" + "\n")
        file2.write("       "+"<ApplicationShortName>"+row[3]+"-"+row[1]+"</ApplicationShortName>"+"\n")
        file2.write("       " +"<ApplicationType>"+row[4]+"</ApplicationType>"+"\n")
        file2.write("       " +"<ParentApplication>"+row[2]+"</ParentApplication>"+"\n")
        file2.write("       " +"<ApplicationLongName>"+row[3]+"-"+row[1]+"</ApplicationLongName>"+"\n")
        file2.write("       " +"<ApplicationGroup>"+row[5]+"</ApplicationGroup>" + "\n")
        file2.write("       " + "<ServerAddresses>"+row[0]+ "</ServerAddresses>" + "\n")
        file2.write("       " + "<ServerPortRange>"+row[1]+"</ServerPortRange>"+"\n")
        file2.write("       " + "<Logged>"+row[6]+"</Logged>"+"\n")
        file2.write("       " + "<ResponseTime>"+row[7]+"</ResponseTime>"+"\n")
        file2.write("       " + "<Session>"+row[8]+"</Session>" + "\n")
      #  file2.write("       " + "<RecordingType>"+row[9]+"</RecordingType>"+"\n")
        file2.write("   " + "</ApplicationConfiguration>" + "\n")
    file.close()
    file2.close()
    # open original file in read mode and new file to write mode
    with open(export_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write begining parm to the new the file
        write_obj.write("<ApplicationConfigurations>" + '\n')
        # Read lines from original file one by one and append them to new file
        for line in read_obj:
            write_obj.write(line)
    # remove original api file
    os.remove(export_file)
    #Append to bottom of file
    with open(dummy_file, "a") as file_object:
        # Append closing of the parm at end of file
        file_object.write("</ApplicationConfigurations>" + "\n")
#run the curl process to import into nG1
headers = {
    'Content-Type': 'application/xml',
}

data = open(dummy_file)
response = requests.post('https://172.23.246.11/ng1api/ncm/applications', headers=headers, data=data, verify=False, auth=('jvigliotti', 'Bat#cave0520'))
