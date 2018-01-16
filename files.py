'''import os
k=os.path.abspath('.')
print(k)
h=os.path.isabs('.')
print(h)
t=os.path.abspath('.\\Scripts')
print(t)
totalsize=0
for f in os.listdir('C:\\Users\\Admin'):
        totalsize=totalsize+os.path.getsize(os.path.join('C:\\Users\\Admin',f))
print(totalsize)
list=os.listdir('C:\\Users\\Admin')
print(list)

los=open('C:\\Users\Admin\\Desktop\\hello.txt')
t=los.read()
print(t)
s=open('hello.txt','a')
s.write('Bacon is a Vegetable')
s.close()
s=open('hello.txt')
k=s.read()
print(k)

import shelve
shelfile=shelve.open('files')
t=['open','close','append']
shelfile['func']=t
shelfile.close()

shelfile=shelve.open('files')
print(type(shelfile))
print(shelfile['func'])
'''
#Quiz File
import random
capitals={'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Create quiz questions and answerkey
for quizNum in range(0,2):
    quizFile=open('C:\\Users\\Admin\\Desktop\\quizfile_%s.txt' %(quizNum+1),'w')
    answerKeyFile=open('C:\\Users\\Admin\\Desktop\\quizanswer_%s.txt' %(quizNum+1),'w')
    quizFile.write('Name:\n\n Date:\n\n Period\n\n')
    quizFile.write((' ' * 20) + 'State Capital Quiz (form%s)' %(quizNum + 1) )
    quizFile.write('\n\n')
    states=list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(50):
        quizFile.write('%s. What is the Capital of %s ?\n' %(questionNum + 1 ,states[questionNum]))
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        for i in range(4):
             quizFile.write('%s. %s\n' %('ABCD'[i] ,answerOptions[i]))
        quizFile.write('\n')
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    #answerKeyFile.write('%s. %s\n' %(questionNum+1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()


