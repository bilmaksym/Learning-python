# The second version of our backup program

import os
import time

source = ['/home/maksym/Desktop/Python']

target_dir = '/home/maksym/Desktop/Backup2'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# The name of the zip file
target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is:\n', zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup failed')
