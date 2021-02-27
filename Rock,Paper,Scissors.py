# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import random
import time
import sys

# GLOBAL VARIABLES SO THEY DO NOT RESET INSIDE THE GAME RESTART LOOP
user_score = 0
computer_score = 0

#this is a helper function to store what a WIN looks like
def is_win(player,opponent):
    #return true if plater wins
    if (player == 'R' and opponent == 'S') or (player == 'P' and opponent == 'R') or (player == 'S' and opponent == 'P'):
        return True

def RPS():
    # IMPORTING THE GLOBAL FUNCTIONS
    global user_score
    global computer_score

    valid_input = ["R","P","S"]
    
    # LOOP FOR USER INPUT VALIDATION
    user_input = False
    while user_input == False:
        user = input("what's your choice? 'R' for rock, 'P' for paper, 'S' for scissors\n:").upper()
        
        # IF GIVEN A VALID INPUT IT WILL BREAK OUT OF THIS LOOP
        if user in valid_input:
            user_input = True
        else:
            print("Please only select either R,P,S")
    
    # ADDED AN ANIMATION TO HELP WITH THE FLOW OF THE GAME, TIMED TO STOP ON GO!

    animation = ["rock","paper","Scissors",'---Go!---']

    for i in range(16):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    # RANDOM COMPUTER CHOICE
    computer = random.choice(['R','P','S'])
    print (f'\n\nYou Picked {user.upper()}\nThe Computer Picks {computer.upper()}')

    # IF DRAW
    if user == computer:
        print("\nit\'s a tie\n")
        #print(f"Your Score {user_score} VS {computer_score} Computer Score")

    # ELSE IF USER WINS
    elif is_win(user,computer):
        user_score += 1
        print("\nYou Won!\n")
        #print(f"Your Score {user_score} VS {computer_score} Computer Score")
    
    # ONLY OPTION LEFT: LOSE
    else:
        computer_score +=1
        print("\nYou Lost!\n")
        #print(f"Your Score {user_score} VS {computer_score} Computer Score")

print('Start New Game?')
start_game = input('Enter "Y" for yes. \nEnter "N" for no. \n:').upper()

while start_game not in ('Y','N'):
    print(f'Your value: {start_game} does not match either option, Try again')
    start_game = input('Enter "Y" for yes. \nEnter "N" for no.\n:').upper()

while start_game == 'Y':
    RPS()
    print("Your Score")
    print(user_score)
    print("Computer Score")
    print(computer_score)

    print ('\ndo you want to go again?')
    start_game = input('Enter "Y" for yes. \nEnter "N" for no.\n:').upper()
        
    while start_game not in ('Y','N'):
        print(f'Your value: {start_game} does not match either option, Try again')
        start_game = input('Enter "Y" for yes. \nEnter "N" for no.\n:').upper()

print('Thanks! Goodbye.')


# %%



