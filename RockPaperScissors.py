import random
import sys
print('ROCK, PAPER ,SCISSORS  GAME'.center(100,' '))
rps = ['rock', 'paper', 'scissor']
computer = random.choice(rps)
player = input("Enter your choice(rock,paper, scissor):").lower()
print(f'You chose:{player}')
print(f'Computer chose: {computer}')
if player not in rps:
    print('Invalid choice')
    sys.exit()
else:

    #Computer chooses rock
    if computer == 'rock':
        if player== 'paper':
            print("You win!")
        elif player == 'scissor':
            print('Computer wins')
        else:
            print('It\'s a tie!')
    #Computer chooses paper
    elif computer == 'paper':
        if player == 'scissor':
            print('You win!')
        elif player == 'rock':
            print('Computer wins')
        else:
            print("It\'s a tie!")
    #Computer chooses scissor
    else:
        if player == 'rock':
            print("You win!")
        elif player == 'paper':
            print('Computer wins')
        else:
            print('It\'s a tie!')

