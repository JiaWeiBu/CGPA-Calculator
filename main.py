import os.path
from fileFx import addData, deleteFiles, displayGPA, editDataFiles, readGpaFile, readStdGpa, readValGpaFile, readValStdGpa, resetProgramme, writeGpaFile, writeStdGPA

def main():
    #check if file present
    if os.path.exists(f'./gpaScore.txt'):
        #yes
        #read the gpaScore and return dictionary
        readValGpaFile()
        d1 = readGpaFile()
    
        #check if record of the past score exist
        if os.path.exists(f'./currentGPA.txt'):
            #yes
            #read the previous record and display the CGPA
            readValStdGpa(d1)
            d2 = readStdGpa()
            displayGPA(d1,d2)
            
            #prompt the past cgpa then ask update or exit
            sentinel = 0
            while not sentinel in ['a','e','d','r','q']: # add edit delete reset
                sentinel = input('\n\nOptions:\n<A>dd new result\n<E>dit current files\n<D>elete file\n<R>eset the programme\n<Q>To quit\n\n<A> <E> <D> <R> <Q> : ').lower()
            
            #check all value for each sentinel    
            if sentinel == 'a':
                addData(d1,d2)
                main()
            elif sentinel == 'e':
                editDataFiles(d1,d2)
                main()
            elif sentinel == 'd':
                deleteFiles()
                main()
            elif sentinel == 'r':
                resetProgramme()
            else:
                quit()
        else:
            #no
            #ask for subject number and result
            writeStdGPA(d1)
            main()
    else:
        #no
        #write a new gpaScore file
        print('Welcome is CGPA calculator, first we need information about your university grading system\n\n')
        writeGpaFile()
        main()

if __name__ == '__main__':
    main()