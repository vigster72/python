import os
backup_path = "/opt/NetScout/rtm/database/dbone"
remote_path = "/opt/backup/backup/SC01"
remote_ip = "172.23.240.42"

os.system ("rsync -Ssav" + " " +backup_path +" " +remote_ip +":" +remote_path)