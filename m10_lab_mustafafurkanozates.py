class Grade:
    def __init__(self, score = 0, examName = 'None'):
        self.score = score
        self.examName = examName

class Student:
    dept = ''

    def __init__(self, name, grades = None):
        self.name = name
        self.grades = grades

    def PrintGradeStats(self, name2):
        maxPoint = 0
        maxExam = ''
        total = 0
        
        for i in self.grades:
            if self.name == name2:
                if i.score > maxPoint:
                    maxPoint = i.score
                    maxExam = i.examName
                total += i.score

        print(f'\tMax grade was in {maxExam} with a score of {maxPoint}')
        
        print(f'\tAverage grade is {total/len(self.grades)}')
        

def welcoming():
    print('\n1. Create a student')
    print('2. Add an exam score for a student')
    print('3. View exam report for a student\n')
    return input('Make a choice: ')

studentList = []

while True:
    welcome = welcoming()
    if welcome == '1':
        studName = input('Enter a student name: ')
        studentList.append(Student(studName))
        print('\nStudent added.')
        
    elif welcome == '2':
        if studentList != []:
            print('Students are listed below:')
            for i, student in enumerate(studentList):
                print(f'{i+1}.', student.name)
            studentChoose = int(input('\nSelect a student: '))
            print('Enter the grade info below.')
            infoName = input('Exam name: ')
            infoScore = int(input('Score: '))
            if studentList[studentChoose-1].grades == None:
                studentList[studentChoose-1].grades = []
            studentList[studentChoose-1].grades.append(Grade(infoScore, infoName))
        else:
            print('\nNo student has been added yet.')

    elif welcome == '3':
        print('Students are listed below:')
        for i, student in enumerate(studentList):
            print(f'{i+1}.', student.name)
        studentChoose = int(input('\nSelect a student: '))

        print(f'\nGrade stats for {studentList[studentChoose-1].name}')
        studentList[studentChoose-1].PrintGradeStats(studentList[studentChoose-1].name)

    else:
        print('End.')
        break

    