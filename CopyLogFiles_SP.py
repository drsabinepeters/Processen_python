### Copying a bunch of log files to the correct directory
import os #importing operating system commands
import shutil # importing shell utilities (for file copying)

source = 'C:/Users/peterss/Dropbox/Work/Python'
destination = 'EC:/Users/peterss/Dropbox/Work/Python/copy'

# create a list from all csv files: (os.listdir(source))

# loop through list: for i in list

# copy item to folder name equal to first 8 characters /log/
## : shutil.copy(source, destination)

for i in sorted(os.listdir(source)):
    subject = i[:8]
    src = source + '/' + i
    des = destination +'/' + subject + '/log'
    try: # This catches errors such cases in which subjects where not part of data, but were in the csv file.
        shutil.copy(src,des)
    except:
        print "Error with participant "+ subject + ", you figure it out!"
