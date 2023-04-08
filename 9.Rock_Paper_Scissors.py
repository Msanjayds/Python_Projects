# Python implementaion of Rock paper and scissors 

import random 

def get_choices():
    player_choice = input("Enter a choice - rock, paper, scissors : ")
    options = ['rock', 'paper','scissors']
    computer_choice = random.choice(options)
    choices={"player": player_choice , "computer" : computer_choice}
    return choices 

def check_win(player,computer):
    print(f"you chose {player} computer chose {computer}")
    if player == computer:
        return 'Its a tie!'
    elif player == 'rock':
        if computer == 'scissors':
            return "Rock smasches Scissors! you win!"
        else:
            return "Paper covers rock! you lose :-("
    elif player == 'paper':
        if computer == 'scissors':
            return "Scissors smasches paper! you lose!"
        else:
            return "Paper covers rock! you win!"
    elif player == 'scissors':
        if computer == 'paper':
            return "Scissors cut paper! you win!"
        else:
            return "Rock smashes scissors! you lose :-("

choices = get_choices()
p_choice = choices["player"]
c_choice = choices["computer"]

result = check_win(p_choice,c_choice)

print(result)



