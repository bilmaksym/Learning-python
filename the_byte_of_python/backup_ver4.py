# The fourth (modified) version of our backup program
__version__ = 1.4

import os
import time
import zipfile

source = '/home/maksym/Desktop/Python'

target_dir = '/home/maksym/Desktop/Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")

comment = input("Enter a comment -->")
if len(comment) == 0:
    target = today + os.sep + now + ".zip"
else:
    target = today + os.sep + "_" + now + comment.replace(" ", "_") + ".zip"

if not os.path.exists(today):
    os.mkdir(today)
    print("Successfully created directory", today)

print("Creating an archive")
zf = zipfile.ZipFile(target, mode='w')

for dirname, subdirs, files in os.walk(source):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()
