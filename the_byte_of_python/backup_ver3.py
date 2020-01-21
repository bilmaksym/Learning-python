# The third version of our backup program

import os
import time

source = ['/home/maksym/Desktop/Python']

target_dir = '/home/maksym/Desktop/Backup3'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip directory
now = time.strftime('%H%M%S')

# Take a comment from the user to create a name of the zip file
comment = input('Enter a comment -->')
# Check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# Run the backup
print('Zip command is:\n', zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup failed')
