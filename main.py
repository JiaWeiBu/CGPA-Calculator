import os.path
from gpaScoreFx import disGpa, readGpaFile, writeGpaFile, writeStdGPA

def main():
    #check if file present
    if os.path.exists(f'./gpaScore.txt'):
        #yes
        #read the gpaScore and return dictionary
        d = readGpaFile()
    
        #check if record of the past score exist
        if os.path.exists(f'./currentGPA.txt'):
            #yes
            #prompt the past cgpa then ask update or exit
            disGpa(d)
            for i in d:
                print(i)
        else:
            #no
            #ask for subject number and result
            writeStdGPA()
            main()
    else:
        #no
        #write a new gpaScore file
        writeGpaFile()
        main()
        
main()