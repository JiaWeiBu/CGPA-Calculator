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
        a = input("Invalid value used, press enter to reset the program")
        quit()

#write student GPA            
def writeStdGPA(d1):
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
    sentinel = 0
    while not sentinel in ['a','b','c','r']:
        sentinel = input('Which file you want to delete?\n<A> Grade Score List\n<B> Your result record\n<C> All the above\n\n<A> <B> <C>: ').lower()
    
    if sentinel == 'a':
        os.remove('gpaScore.txt')
    elif sentinel == 'b':
        os.remove('currentGPA.txt')
    elif sentinel == 'r':
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
    sentinel = 0
    while sentinel in ['a','b','r']:
        sentinel = input('Which file you want to delete?\n<A> Grade Score List\n<B> Your result record\n\n<A> <B>: ').lower()
    
    if sentinel == 'r':
        resetProgramme()
    elif sentinel == 'a':
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
            a = input("Invalid value used, press enter to reset the program")
            quit()
    else:
        #creat the gpa score list
        gpaFile = open('currentGPA.txt','w')
        
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
def editDataFiles():
    pass