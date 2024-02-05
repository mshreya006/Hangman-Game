# CONNECTING PYTHON WITH MYSQL

import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",password='Ramans@123',database='hangman')
Cursor = conn.cursor()
print("LET'S PLAY HANGMAN!")
username = input("enter username")

# MENU

print("1.create new account")
print("2.login")
choice = int(input("enter your choice(1/2):"))

# CREATING AN ACCOUNT

if choice ==1:
        name = input("enter name:")
        email_id = input("enter emailid:")
        points = 0
        Cursor.execute("insert into players values('"+name+"','"+email_id+"','"+str(points)+"')")
        conn.commit()
        print("account created")
        move_in=input("press enter to login")

elif choice==2:
        email_id=input("enter email")
        pwd=input("enter password")
        Cursor.execute('select*from players where name="'+email_id+" and pwd='"+pwd+'"')

import random
from words import LIST
from collections import Counter
x = random.choice(LIST)
print("let's begin! HINT: Indian tourist cities")

for i in x:
        print('_', end = ' ')
print()

# GUESSING THE WORD

playing = True
letterguessed = ''
chances = len(x) + 7
correct = 0
score = 0

try :
        while(chances !=0) and score == 0:
                print()
                chances -= 1
                try:
                        guess = input('Enter your Guess:')
                except:
                        print('Enter only a letter!')
                if not guess.isalpha():
                        print('ENTER ONLY A LETTER')
                        continue
                elif len(guess)>1:
                        print('enter only single letter')
                elif guess in letterguessed:
                        print('you have already guessed this letter')


                if guess in x:
                        a= x.count(guess)
                        for _ in range(a):
                                letterguessed += guess

                        for char in x:
                                if char in letterguessed and Counter(letterguessed) != Counter(x):
                                        print(char, end = ' ')
                                        correct += 1

                                elif Counter(letterguessed) == Counter(x):
                                        print('the word is:',x, end = ' ')
                                        score = 1
                                        print("\n",'yay! you found the word!')
                                        print("your score is 100")

                                        sql = ("update players set points = points+100 where name = ('"+name+"')")
                                        Cursor.execute(sql)
                                        conn.commit()
                                        break
                                        break

                                else:
                                        print('_' , end = ' ')

                if chances <= 0 and Counter(letterguessed) != Counter(x):
                        print()
                        print('you lost! better luck next time')
                        print("your score is 0")
                        print('The word was {}'.format(x))

except KeyboardInterrupt:
                print('Adios!')
                exit()
