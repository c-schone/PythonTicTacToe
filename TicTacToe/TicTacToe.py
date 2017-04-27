# Tic Tac Toe game for Python Bootcamp
# Player 1: x
# Player 2: o
import random

def run_game(player):
    print('Player ', player, 'is first!')
    grid = ['[1]', '[2]', '[3]', '[4]', '[5]', '[6]', '[7]', '[8]', '[9]']
    print('', grid[0], grid[1], grid[2], '\n', grid[3], grid[4], grid[5], '\n',
          grid[6], grid[7], grid[8])
    ingame = True
    counter = 0
    while (ingame):
        print('Turn Player ', player, ':')
        field = 0
        field = int(input('Choose field:'))
        while (field < 1 or field > 9):
            field = int(input('Wrong input! Choose field:'))
        field -= 1
        if (player == 1):
            grid[field] = '[x]'
        elif (player == 2):
            grid[field] = '[o]'
        print('', grid[0], grid[1], grid[2], '\n', grid[3], grid[4], grid[5], '\n',
          grid[6], grid[7], grid[8])
        if (grid[0] == grid[1] == grid[2] or
           grid[0] == grid[4] == grid[8] or
           grid[0] == grid[3] == grid[6] or
           grid[1] == grid[4] == grid[7] or
           grid[3] == grid[4] == grid[5] or
           grid[2] == grid[5] == grid[8] or
           grid[2] == grid[4] == grid[6] or
           grid[6] == grid[7] == grid[8]):
            print('Player ', player, ' won!')
            ingame = False
        else:
            counter += 1
            if (counter >= 9):
                print('Draw game!')
                ingame = False
            player = (player % 2) + 1
    restart_game(player)

def restart_game(player):
    restart = input('Restart: y or n?')
    if (restart == 'y'):
        player = (player % 2) + 1
        run_game(player)

print('Hello and welcome to Tic Tac Toe!')
input('Ready to start? Press return!')
player = random.randint(1,2)
run_game(player)       
