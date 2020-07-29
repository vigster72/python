import os
#def prepend_line("/home/netscout/Downloads/test1.txt", "<ApplicationConfigurations>" + "\n")
dummy_file = "/home/netscout/Downloads/test3.txt"
    # open original file in read mode and dummy file in write mode
with open("/home/netscout/Downloads/test1.txt", 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write("<ApplicationConfigurations>" + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
os.remove("/home/netscout/Downloads/test1.txt")
    # Rename dummy file as the original file
   # os.rename(dummy_file, file_name)
with open("/home/netscout/Downloads/test3.txt", "a") as file_object:
    # Append 'hello' at the end of file
    file_object.write("</ApplicationConfigurations>" + "\n")
#os.system("curl -X POST -u administrator:netscout1 -d @test3.txt -k https://192.168.87.245:8443/ng1api/ncm/applications -H 'Content-Type:application/xml'")
os.system(‘open ‘+ filepath)