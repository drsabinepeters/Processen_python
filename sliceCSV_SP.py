### sliceCSV, create seperate files for each subject
import csv

csvFile = 'C:/Users/peterss/CSVfilesmaken/T1_klaarvoorcsv.csv'
destination = 'C:/Users/peterss/CSVfilesmaken/test/'
readCSV = open(csvFile,'r')

# Read header line, for pasting in every new log file (strip removes newline symbol, split, creates a list just to make life easier).
FirstLine = readCSV.readline().strip().split(',') 
csvRead = readCSV.read()
CSV = csvRead.split('\n')
TP = '1' # Timepoint as string
sub = 0

for line in CSV:
    if line != '': 
        Split=line.split(',')
        newSub = Split[0]
        if newSub != sub: # If we reach a new subject
            if file in locals(): # Just a catch for the first participant
                file.close()                            
            # Create a new csv file for new subject
            sub = newSub
            if len(newSub) < 4:                
                file = open(destination +'BT'+TP+'P0'+newSub+'_6types.csv','wb') # use CSV variant       
            else: 
                file = open(destination +'BT'+TP+'P'+newSub+'_6types.csv','wb') # use CSV variant                       
            logWriter = csv.writer(file, delimiter=',')
            logWriter.writerow(FirstLine)
        print(Split)
        logWriter.writerow(Split) # Write a new line in any event.
        
    else: # We have reached the final line in the file.
        file.close()

readCSV.close()