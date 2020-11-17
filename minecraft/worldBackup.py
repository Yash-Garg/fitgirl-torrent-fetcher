# A script to backup my world and upload it to telegram

import os
import zipfile
import subprocess
from datetime import datetime
import pytz

now = str(datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S"))
zipname = "world_" + now + ".zip"
zf = zipfile.ZipFile(zipname, "w")
print("\nMinecraft World Backup Created at " + now)
for dirname, subdirs, files in os.walk("world"):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()
print("\nStarting upload to telegram\n")
subprocess.run(["telegram-upload", "-d", zipname])
print("\nBackup Uploaded Successfully!")
