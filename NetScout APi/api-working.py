import csv
file2 = open(r"/home/netscout/Downloads/test1.txt","w")
with open('/home/netscout/Downloads/api-test.csv', 'r') as file:
    reader = csv.reader(file,delimiter = ',',skipinitialspace=True)
    for row in reader:
       # file2.write("<ApplicationConfigurations>"+"\n")
        file2.write("   "+"<ApplicationConfiguration>" + "\n")
        file2.write("       "+"<ApplicationShortName>"+"Hadoop-"+row[1] + "</ApplicationShortName>"+"\n")
        file2.write("       " + "<ApplicationType>Server-based Apps</ApplicationType>"+"\n")
        file2.write("       " + "<ParentApplication>TCP</ParentApplication>" + "\n")
        file2.write("       " + "<ApplicationLongName>" + "Hadoop-" + row[1] + "</ApplicationLongName>" + "\n")
        file2.write("       " + "<ApplicationGroup>Other</ApplicationGroup>" + "\n")
        file2.write("       " + "<ServerAddresses>"+row[0]+row[2]+"</ServerAddresses>"+ "\n")
        file2.write("       " + "<ServerPortRange>"+row[1]+"</ServerPortRange>"+ "\n")
        file2.write("   " + "</ApplicationConfiguration>" + "\n")
       # file2.write("</ApplicationConfigurations>" + "\n")
