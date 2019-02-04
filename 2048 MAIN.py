"""
Created on Feb 3 2019
@author: jihwanshin
"""

import random

"""
This program recreates 2048. Notes for this project will be written here

https://en.wikipedia.org/wiki/2048_(video_game)#Gameplay

FUNCTIONS TO MAKE
initialise(), V
show(), V
move(), 
up(),
down(),
left(),
right()
check2048()

while not check2048(board):
    show()
    move()
    
could add score system after finishing 
"""

print("* Hi! This is a recreation of the game 2048 on Python. Have fun! *")  # starting message
board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]  # initial starting board


def show():
    for row in board:
        print(*row)


def up():
    pass


def down():
    pass

# HOW ABOUT MOVING ALL ZEROES TO THE BACK???
def left():  # it can now move rows with ONE number
    for i in range(4):
        for number in board[i]:
            if number == 0:
                continue
            else:
                board[i][board[i].index(number)] = 0
                board[i][0] = number
                break


def right():
    pass


def move(direction):
    if direction == "up":
        up()
    if direction == "down":
        down()
    if direction == "left":
        left()
    if direction == "right":
        right()
    while True:  # this will randomly choose where the new number will appear
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if board[x][y] == 0:
            break
        else:
            continue
    twofour = random.choices(  # this will randomly choose the new number that will appear
        population = [2, 4],  # 75% of the time it will be 2, 25% of the time it will be 4
        weights = [0.75, 0.25]
    )
    board[x][y] = twofour[0]

move(left)
show()
