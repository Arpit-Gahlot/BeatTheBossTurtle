import mysql.connector
from turtle import *

# introduction
print('Welcome to \'Beat the Boss\'! In this game you have to answer\n\
questions currently to decrease the boss\' health and defeat him')
print('\n')

# connect to the database
databasePassword = input('To begin, enter the root@localhost password to connect to the database:')
myDB = mysql.connector.connect(host='localhost',
                               user='root',
                               passwd=databasePassword)

# Create a cursor object
myCursor = myDB.cursor()
myCursor.execute("CREATE DATABASE IF NOT EXISTS game1")
myCursor.execute("USE game1")

print('Successfully connected to the localhost! Enter your name below once your\'re ready')
print('\n')
name = input('Enter your name:')
print('Now switch to the window which just opened')


# Draw the game visuals
title('Game window')
reset()
Screen()
bgpic('Images/Mordekaiser.png')
up()
hideturtle()
style = ('Arial', 50, 'bold')
color('white')
write('Current Boss Health', font = style, align = 'center')
up()
goto(-320, -50)
width(70)
color('green')
down()
forward(640)
up()
goto(-320, -80)
style2 = ('Arial', 36)
color('white')
goto(350, -150)
down()
backward(700)
up()
goto(0, -180)
color('royalblue1')
write('The boss is at 100% HP', font=style2, align = 'center')
hideturtle()

# The Lists of questions and answers
questionsList = ['what is the square root of 169?',
                 'which game recently crossed 1 trillion views on Youtube?',
                 'Which is the only mammal that can fly?',
                 'Which is the hottest planet in the Solar system?',
                 'Which is the largest bone in the human body?']

answersList = ['13', 'minecraft', 'bat', 'venus', 'femur']

# The main game logic
numberOfCorrectAnswers = 0
for i in range(len(questionsList)):

    if numberOfCorrectAnswers == 4:
        break

    else:
        userAnswer = textinput(str(i + 1) + 'st question', questionsList[i])

        # If the user correctly answers
        if userAnswer == answersList[i]:
            color('white')
            goto(350, -150)
            down()
            backward(700)
            up()
            goto(0,-180)
            color('royalblue1')
            write('Good Job! The boss is at ' + str(100 - round(25 * (numberOfCorrectAnswers + 1))) + '% HP',
                  font=style2, align='center')
            x = 320 - numberOfCorrectAnswers * 25 * 6.4
            goto(x, -50)
            width(70)
            color('white')
            down()
            backward(160)
            up()
            numberOfCorrectAnswers = numberOfCorrectAnswers + 1

        # If the answer is incorrect
        else:
            color('white')
            goto(350, -150)
            down()
            backward(700)
            up()
            goto(0, -180)
            color('red')
            write('Incorrect answer', font=style2, align='center')

# If 4 answers are correctly answered, the user has won the game
if numberOfCorrectAnswers == 4:
    color('white')
    goto(350, -150)
    down()
    backward(700)
    up()
    goto(0, -180)
    color('royalblue1')
    write('You defeated the boss!', font=style2, align='center')

# If 3 or fewer answers are correctly answered, the user has lost the game
else:
    color('white')
    goto(350, -150)
    down()
    backward(700)
    up()
    goto(0, -180)
    color('red')
    write('You lost the game', font=style2, align='center')

# Upload the scores to the connected database
data = "insert into scores values(%s, %s)"
myCursor.execute(data,(name, numberOfCorrectAnswers))
myDB.commit()

# Display the scores of the players who have played the game so far
print('scores of the players are:-')
print('Name\tScore')
myCursor.execute('select * from scores')
results = myCursor.fetchall()
for j in results:
    print(j[0] + '\t' + str(j[1]))
print('Thanks for playing!')
