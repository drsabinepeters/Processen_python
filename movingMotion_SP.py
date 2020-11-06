### This script will look through the subject folders, 
### find the txt file with motion information and 
### copy it up one folder in the hierarchy

#aanpassing Sabine: nu voor analyse met motion regressors, voor BT3 move ik de rp_af files van bold/ naar bold/run1

import os

source = "E:/BT3Processed"
# "E:/BT3Processed/backup/Excluded" ## Test environment
#"E:/BT3Processed"
os.chdir(source)

# Iterate over folders having with BT in its name
for dir in sorted(os.listdir(source)):
    if "BT3" in dir:
        longDir1 = dir + "/bold"
        if os.path.isfile(longDir1+"/rp_af_"+dir+"_run1_001.txt"):
            print "Found " + longDir1+"/rp_af_"+dir+"_run1_001.txt"
            os.rename(longDir1+"/rp_af_"+dir+"_run1_001.txt", dir + "/bold/run1/rp_af_" + dir + "_run1_001.txt")
       
