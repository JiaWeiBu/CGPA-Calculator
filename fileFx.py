import os

#validator for GPA file
def readValGpaFile():
    #open file
    gpaFile = open('gpaScore.txt', 'r') 
    #get grade and define points variable, while loop to get all the data out of the file
    grade = gpaFile.readline()
    
    #check if file is empty from begining
    if grade == '':
        gpaFile.close()

        #write GPA file function
        writeGpaFile()
        return
    else:
        gpaFile.close()
        return

#read GPA file
def readGpaFile():
    #open file
    gpaFile = open('gpaScore.txt', 'r')
    
    #create a dictionary d
    d = {}
    
    #get grade and define points variable, while loop to get all the data out of the file
    grade = gpaFile.readline()
        
    #write the GPA file
    while grade != '':
        #read the quantity
        gpaPoints = float(gpaFile.readline())
        
        #remove the \n
        grade = grade.rstrip('\n')
        
        #add to dictionary
        d[grade] = gpaPoints
        
        #read the next file, if false the loop end
        grade = gpaFile.readline()
        
    #close the file
    gpaFile.close()
    
    return d

#clear the screen
def screenClear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

#display GPA from a dictionary
def disGpa(d):
    #display the inputed gpa value
    print('Grade\tPoints')
    for key,value in d.items():
        print(f'{key}\t{value:.4f}')
            
    #space bar
    print('')
    return

#display student grade from a dictionary
def disGrade(d):
    #display the inputed gpa value
    print('Subjects\t\tGrade')
    for key,value in d.items():
        print(f'{key}\t{value}')
            
    #space bar
    print('')
    return

#write gpa file
def writeGpaFile():
    try:
        #creat the gpa score list
        gpaFile = open('gpaScore.txt','w')
        
        #sentinel key and start keyin data
        count = 'y'
        
        #dictionary display
        d = {}
        
        while count == 'y':
            #display gpa
            if d:
                disGpa(d)
            
            #get the grade
            grade = input('What is the grade: ')
            gpaPoints = float(input(f'What is the grade({grade}) GPA points: '))
            
            #add to dictionary
            d[grade] = gpaPoints
            
            #add \n
            grade += '\n'
            gpaPoints = str(gpaPoints) + '\n'
            
            #write into the file
            gpaFile.write(grade)
            gpaFile.write(gpaPoints)
            
            #sentinel validator
            count = input('Do you want to add more to the score? Y/n ').lower()
            while not count in ['y','n','r']:
                count = input('Error: Incorrect syntax used.\nDo you want to add more to the score? Y/n ').lower()
            
            if count == 'n':
                gpaFile.close()
                screenClear()
            elif count == 'r':
                gpaFile.close()
                resetProgramme()
            else:
                screenClear()
    except ValueError:
        enter = input("Invalid value used, press enter to reset the program")
        quit()

#write student GPA            
def writeStdGPA(d1):
    #display the grade currently have
    disGpa(d1)
    
    #greetings setup
    print('I would need you to key in the your subject name and your grade\n')

    #creat the gpa score list
    gpaFile = open('currentGPA.txt','w')
    
    #sentinel key and start keyin data
    count = 'y'
    
    #dictionary display
    d = {}
    
    while count == 'y':
        #display gpa
        if d:
            disGrade(d)
        
        #get the grade
        subject = input('What is the subject name: ')
        grade = input(f'What is the subject ({subject}) grade: ')
        
        while not (grade in d1.keys() or grade in ['r','R']):
            grade = input(f'Grade not found: What is the subject ({subject}) grade: ')
        
        #reset
        if grade in ['r','R']:
            gpaFile.close()
            resetProgramme()

        #add to dictionary
        d[subject] = grade
        
        #add \n
        subject += '\n'
        grade += '\n'
        
        #write into the file
        gpaFile.write(subject)
        gpaFile.write(grade)
        
        #sentinel validator
        count = input('Do you want to add more to the score? Y/n ').lower()
        while not count in ['y','n','r']:
            count = input('Error: Incorrect syntax used.\nDo you want to add more to the score? Y/n ').lower()
        
        if count == 'n':
            gpaFile.close()
            screenClear()
        elif count == 'r':
            gpaFile.close()
            resetProgramme()
        else:
            screenClear()

#validator student GPA file
def readValStdGpa(d):
    #open file
    gpaFile = open('currentGPA.txt', 'r') 
    #get grade and define points variable, while loop to get all the data out of the file
    subject = gpaFile.readline()
    
    #check if file is empty from begining
    if subject == '':
        gpaFile.close()

        #write GPA file function
        writeStdGPA(d)
        return
    else:
        gpaFile.close()
        return
            
def readStdGpa():
    #open file
    gpaFile = open('currentGPA.txt', 'r')
    
    #create a dictionary d
    d = {}
    
    #get grade and define points variable, while loop to get all the data out of the file
    subject = gpaFile.readline()
        
    #write the GPA file
    while subject != '':
        #read the quantity
        grade = gpaFile.readline()
        
        #remove the \n
        subject = subject.rstrip('\n')
        grade = grade.rstrip('\n')
        
        #add to dictionary
        d[subject] = grade
        
        #read the next file, if false the loop end
        subject = gpaFile.readline()
        
    #close the file
    gpaFile.close()
    
    return d

#display GPA
def displayGPA(d1,d2):
    #constant value
    GPA = 0
    count = 0
    
    #get all value of GPA
    for key in d2:
        count += 1
        GPA += d1[d2[key]]
    
    #get average
    GPA /= count
    
    #display
    disGrade(d2)
    print(f'\nYour current CGPA is {GPA:.4f}')
    
    return 

#delete files
def deleteFiles():
    screenClear()
    
    #ask for which files to delete
    sentinel8 = 0
    while not sentinel8 in ['a','b','c','r']:
        sentinel8 = input('Which file you want to delete?\n<A> Grade Score List\n<B> Your result record\n<C> All the above\n\n<A> <B> <C>: ').lower()
    
    if sentinel8 == 'a':
        os.remove('gpaScore.txt')
    elif sentinel8 == 'b':
        os.remove('currentGPA.txt')
    elif sentinel8 == 'r' or sentinel8 == 'c':
        resetProgramme()
    else:
        enter = input('Error: Please backup both .txt file and press enter restart the programme')
    
    #exit function
    return

#reset the programme
def resetProgramme():
    #check if files are present
    if not (os.path.exists('gpaScore.txt') and os.path.exists('currentGPA.txt')):
        if os.path.exists('gpaScore.txt'):
            os.remove('gpaScore.txt')
            quit()
        else:
            os.remove('currentGPA.txt')
            quit()
    else:
        #remove all user generated files
        os.remove('gpaScore.txt')
        os.remove('currentGPA.txt')
        quit()
        
#add the data
def addData(d1,d2):
    screenClear()
    sentinel7 = 0
    while not sentinel7 in ['a','b','r']:
        sentinel7 = input('Which file you want to add?\n<A> Grade Score List\n<B> Your result record\n\n<A> <B>: ').lower()
    
    if sentinel7 == 'r':
        resetProgramme()
    elif sentinel7 == 'a':
        try:
            #creat the gpa score list
            gpaFile = open('gpaScore.txt','a')
            
            #sentinel key and start keyin data
            count = 'y'
            
            #dictionary display
            d = d1
            
            while count == 'y':
                #display gpa
                if d:
                    disGpa(d)
                
                #get the grade
                grade = input('What is the grade: ')
                gpaPoints = float(input(f'What is the grade({grade}) GPA points: '))
                
                #add to dictionary
                d[grade] = gpaPoints
                
                #add \n
                grade += '\n'
                gpaPoints = str(gpaPoints) + '\n'
                
                #write into the file
                gpaFile.write(grade)
                gpaFile.write(gpaPoints)
                
                #sentinel validator
                count = input('Do you want to add more to the score? Y/n ').lower()
                while not count in ['y','n','r']:
                    count = input('Error: Incorrect syntax used.\nDo you want to add more to the score? Y/n ').lower()
                
                if count == 'n':
                    gpaFile.close()
                    screenClear()
                elif count == 'r':
                    gpaFile.close()
                    resetProgramme()
                else:
                    screenClear()
        except ValueError:
            enter = input("Invalid value used, press enter to reset the program")
            quit()
    else:
        #creat the gpa score list
        gpaFile = open('currentGPA.txt','a')
        
        #sentinel key and start keyin data
        count = 'y'
        
        #dictionary display
        d = d2
        
        while count == 'y':
            #display gpa
            if d:
                disGrade(d)
            
            #get the grade
            subject = input('What is the subject name: ')
            grade = input(f'What is the subject ({subject}) grade: ')
            
            while not (grade in d1.keys() or grade in ['r','R']):
                grade = input(f'Grade not found: What is the subject ({subject}) grade: ')
            
            #reset
            if grade in ['r','R']:
                gpaFile.close()
                resetProgramme()

            #add to dictionary
            d[subject] = grade
            
            #add \n
            subject += '\n'
            grade += '\n'
            
            #write into the file
            gpaFile.write(subject)
            gpaFile.write(grade)
            
            #sentinel validator
            count = input('Do you want to add more to the score? Y/n ').lower()
            while not count in ['y','n','r']:
                count = input('Error: Incorrect syntax used.\nDo you want to add more to the score? Y/n ').lower()
            
            if count == 'n':
                gpaFile.close()
                screenClear()
            elif count == 'r':
                gpaFile.close()
                resetProgramme()
            else:
                screenClear()
    return

#edit the files
def editDataFiles(d1,d2):
    screenClear()
    sentinel9 = 0
    #ask for action
    while not sentinel9 in ['a','b','r']:
        sentinel9 = input('Which file you want to edit?\n<A> Grade Score List\n<B> Your result record\n\n<A> <B>: ').lower()
    
    if sentinel9 == 'r':
        resetProgramme()
    elif sentinel9 == 'a':
        sentinel2 = 0
        while not sentinel2 in ['c','a','d']:
            sentinel2 = input('\n\nDo you wish to:\n<C>hange the value\n<A>dd a value\n<D>elete a value\n<C> <A> <D>: ').lower()
        
        if sentinel2 == 'c':
            #display the dictionary
            disGpa(d1)
            
            #which do you want to change
            sentinel3 = 0
            while not sentinel3 in ['g','p']:
                sentinel3 = input('\nWhich value do you want to change <G>rade or <P>oint: ')
            
            #grade or point
            #change the grade
            if sentinel3 == 'g':
                sentinel4 = '_'
                while not sentinel4 in d1:
                    sentinel4 = input('Which grade do you want to change: ')
                
                #get new value
                newVal = input('What value do you want to change to: ')
                value = d1[sentinel4]
                
                #delete key
                del(d1[sentinel4])
                
                #assign new value
                d1[newVal] = value
                
                #from dictionary to new file
                dicToFile(d1,'gpaScore.txt')
                return
            #chang the point
            else:
                try:
                    sentinel4 = '_'
                    while not sentinel4 in d1:
                        sentinel4 = input('Which value do you want to change (Type in the grade): ')
                    
                    #get new value
                    newVal = float(input('What value do you want to change to: '))
                    d1[sentinel4] = newVal
                    
                    #from dictionary to new file
                    dicToFile(d1,'gpaScore.txt')
                    return
                except ValueError:
                    enter = input('Error: Must use a float number')
                    return
        #add value
        elif sentinel2 == 'a':
            addData(d1,d2)
            return
        #delete value 'd'
        else:
            #display the dictionary
            disGpa(d1)
            
            #grade
            sentinel4 = '_'
            while not sentinel4 in d1:
                sentinel4 = input('Which grade do you want to delete: ')
                
            #delete key
            del(d1[sentinel4])
                
            #from dictionary to new file
            dicToFile(d1,'gpaScore.txt')
            return
    
    #current GPA file 'b'
    else:
        sentinel2 = 0
        while not sentinel2 in ['c','a','d']:
            sentinel2 = input('\n\nDo you wish to:\n<C>hange the value\n<A>dd a value\n<D>elete a value\n<C> <A> <D>: ').lower()
        
        if sentinel2 == 'c':
            #display the dictionary
            disGrade(d2)
            
            #which do you want to change
            sentinel3 = 0
            while not sentinel3 in ['s','g']:
                sentinel3 = input('\nWhich value do you want to change <S>ubject or <G>rade: ')
            
            #grade or point
            #change the grade
            if sentinel3 == 's':
                sentinel4 = '_'
                while not sentinel4 in d2:
                    sentinel4 = input('Which subject do you want to change: ')
                
                #get new value
                newVal = input('What grade do you want to change to: ')
                value = d2[sentinel4]
                
                #delete key
                del(d2[sentinel4])
                
                #assign new value
                d2[newVal] = value
                
                #from dictionary to new file
                dicToFile(d2,'currentGPA.txt')
                return
            #chang the point
            else:
                #get the subject
                sentinel4 = '_'
                while not sentinel4 in d2:
                    sentinel4 = input('Which grade do you want to change (Type in the subject): ')
                
                #get new value
                newVal = input('What value do you want to change to: ')
                d2[sentinel4] = newVal
                
                #from dictionary to new file
                dicToFile(d2,'currentGPA.txt')
                return
                
        #add value
        elif sentinel2 == 'a':
            addData(d1,d2)
            return
        #delete value 'd'
        else:
            #display the dictionary
            disGrade(d2)
            
            #grade
            sentinel4 = '_'
            while not sentinel4 in d2:
                sentinel4 = input('Which grade do you want to delete: ')
                
            #delete key
            del(d2[sentinel4])
                
            #from dictionary to new file
            dicToFile(d2,'currentGPA.txt')
            return

#from dictionary data turn into file
def dicToFile(d1,filename):
    #creat the new file
    gpaFile = open('temp.txt','w')
    
    for key,value in d1.items():
        #assign value
        grade = key
        gpaPoints = value
        
        #add \n
        grade += '\n'
        gpaPoints = str(gpaPoints) + '\n'
        
        #write into the file
        gpaFile.write(grade)
        gpaFile.write(gpaPoints)
        
    #close file
    gpaFile.close()
    
    #delete the original file
    os.remove(filename)
    
    #rename the file
    os.rename('temp.txt',filename)
    screenClear()
    return