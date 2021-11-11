import os

def readGpaFile():
    #open file
    gpaFile = open('gpaScore.txt', 'r')
    
    #create a dictionary d
    d = {}
    
    #get grade and define points variable, while loop to get all the data out of the file
    grade = gpaFile.readline()
    
    #check if file is empty from begining
    if grade == '':
        gpaFile.close()

        #write GPA file function
        writeGpaFile()
        
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

def writeGpaFile():
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
        while count != 'y' and count != 'n':
            count = input('Error: Incorrect syntax used.\nDo you want to add more to the score? Y/n ').lower()
        
        if count == 'n':
            gpaFile.close()
            screenClear()
        else:
            screenClear()
            
def writeStdGPA():
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
        while count != 'y' and count != 'n':
            count = input('Error: Incorrect syntax used.\nDo you want to add more to the score? Y/n ').lower()
        
        if count == 'n':
            gpaFile.close()
            screenClear()
        else:
            screenClear()