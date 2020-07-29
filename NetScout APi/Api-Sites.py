import csv
import os
import requests
import_file = '/home/netscout/Downloads/site-import.csv'
export_file = '/home/netscout/Downloads/site-api2.txt'
dummy_file = "/home/netscout/Downloads/site-api-input1.txt" # This file is what will used in the curl
user_name = 'jvigliotti'
user_pass = 'Bat#cave0520'
server_ip = '172.23.246.11'
server_port = '443'
file2 = open(export_file,"w") #Creates the Api import file
with open(import_file , 'r') as file:  # This csv data import to with Api
    reader = csv.reader(file,delimiter = ',',skipinitialspace=True)
    #This creating the xml for the SBA import
    for row in reader:
        file2.write("   " + "<site>" + "\n")
        file2.write("       " + "<addresses>"+"\n")
        file2.write("         " + "<address>" + row[0] + "</address>" + "\n")
        if row[3]:
            file2.write("         " + "<address>" + row[3] + "</address>" + "\n")
        if row[4]:  # in (None,""):
            file2.write("         " + "<address>" + row[4] + "</address>" + "\n")
       # if row[5]:  # in (None, ""):
        #    file2.write("         " + "<address>" + row[5] + "</address>" + "\n")
       # if row[6]:  # in (None, ""):
       #     file2.write("         " + "<address>" + row[6] + "</address>" + "\n")
       # if row[7]:  # in (None, ""):
       #     file2.write("         " + "<address>" + row[7] + "</address>" + "\n")
       # if row[8]:  # in (None, ""):
        #    file2.write("         " + "<address>" + row[8] + "</address>" + "\n")
       # if row[9]:  # in (None, ""):
        #    file2.write("         " + "<address>" + row[9] + "</address>" + "\n")
       # if row[10]:
       #     file2.write("         " + "<address>" + row[10] + "</address>" + "\n")
       # if row[11]:  # in (None,""):
        #    file2.write("         " + "<address>" + row[11] + "</address>" + "\n")
       # if row[12]:  # in (None, ""):
       #     file2.write("         " + "<address>" + row[12] + "</address>" + "\n")
       # if row[13]:  # in (None, ""):
        #    file2.write("         " + "<address>" + row[13] + "</address>" + "\n")
       # if row[14]:  # in (None, ""):
       #     file2.write("         " + "<address>" + row[14] + "</address>" + "\n")
       # if row[15]:  # in (None, ""):
       #     file2.write("         " + "<address>" + row[15] + "</address>" + "\n")
       # if row[16]:  # in (None, ""):
        #    file2.write("         " + "<address>" + row[16] + "</address>" + "\n")
       # if row[17]:  # in (None, ""):
       #     file2.write("         " + "<address>" + row[17] + "</address>" + "\n")
        #if row[18]:  # in (None, ""):
        #    file2.write("         " + "<address>" + row[18] + "</address>" + "\n")
       # if row[19]:  # in (None, ""):
        #    file2.write("         " + "<address>" + row[19] + "</address>" + "\n")
        file2.write("       " + "</addresses>" + "\n")
        file2.write("       " + "<speedKbps>"+row[2]+"</speedKbps>"+"\n")
        file2.write("       " + "<name>"+row[1]+"</name>"+"\n")
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


headers = {
    'Content-Type': 'application/xml',
}

data = open(dummy_file)
response = requests.post('https://'+server_ip+'/ng1api/ncm/sites', headers=headers, data=data, verify=False, auth=(user_name, user_pass))

