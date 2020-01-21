import os
import time

# 1. The files and directories are specified in a list
source = ['/home/maksym/Desktop/Python']
# We have to use double quotes inside a string for names with spaces in it. Also we can use a raw string.

# 2. The backup must be stored in a main backup directory
target_dir = '/home/maksym/Desktop/Backup'

# 3. The files are backed up into a zip file
# 4. The name of the zip archive is the current date and time
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

# 5. We use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# Run the backup
print('Zip command is:\n', zip_command)
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup failed')

