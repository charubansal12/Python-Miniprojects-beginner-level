import random
import simplegui
import math

rem1=7
rem2=10
rem=rem1
flag1=0
flag2=0
print "The default range is 0-100. Push the button to select appropriate range"

def new_game():
    global secret_number,rem,rem1,rem2
    if(flag1==1)and(flag2==0):
        rem=rem1
    elif(flag1==0)and(flag2==1):
        rem=rem2
    
    secret_number=random.randrange(0,100)
    print "Number of remaining guesses is %d" % rem

def range100():
   
    global flag1,secret_number
    flag1=1
    flag2=0
    new_game()
    secret_number=random.randrange(0,100)
    print "New range is 0-100. Guess a number between 0 and 99"
    

def range1000():
     
    global flag2,secret_number
    flag2=1
    flag1=0
    new_game() 
    secret_number=random.randrange(0,1000)
    print "New range is 0-1000. Guess a number between 0 and 999"
    
   
    
def input_guess(guess):
    global rem
    rem=rem-1
    if(rem<=0):
        print "Game terminated. You lost. Press 'run' to restart game"
    else:
        
        guess=int(guess)
        print "Guess was %d "% guess
        if guess==secret_number:
            new_game()
            print "Correct!"
            print "You won.We begin a new game now."
           
        elif guess>secret_number:
            print "Higher"
        else:
             print "Lower"
        print "Number of remaining guesses is %d" %rem
    
    
f=simplegui.create_frame('Guess a number',200,200,100)


f.add_button("Range:0 - 100",range100,100)
f.add_button("Range:0 - 1000",range1000,100)
f.add_input("Enter here",input_guess,100)
f.start()


new_game()

