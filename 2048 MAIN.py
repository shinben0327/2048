"""
Created on Feb 3 2019
@author: jihwanshin
"""

import random
import sys

"""
This program recreates 2048. Notes for this project will be written here

https://en.wikipedia.org/wiki/2048_(video_game)#Gameplay

FUNCTIONS TO MAKE
initialise(), V
show(), V
move(), 
up(),
down(),
left(), V
right()
check2048() V

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


def left():
    for row in board:
        # this moves all the numbers
        counter = 0
        if row[3] == 0:
            row.remove(row[3])
            counter += 1
        if row[2] == 0:
            row.remove(row[2])
            counter += 1
        if row[1] == 0:
            row.remove(row[1])
            counter += 1
        if row[0] == 0:
            row.remove(row[0])
            counter += 1
        # this combines the numbers if they are identical
        for i in range(len(row)-1):
            if row[i] == row[i+1]:
                row[i] = row[i]*2
                del row[i+1]
                row.append(0)
        # this makes sure that the row still has four numbers
        for i in range(counter):
            row.append(0)


def right():
    pass


def gamequit():
    sys.exit("THANKS FOR PLAYING!")


def newrandnum():
    while True:  # this will randomly choose where the new number will appear
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if board[x][y] == 0:
            break
        else:
            continue
    twofour = random.choices(  # this will randomly choose the new number that will appear
        population=[2, 4],  # 75% of the time it will be 2, 25% of the time it will be 4
        weights=[0.75, 0.25]
    )
    board[x][y] = twofour[0]


def move(direction=input("Please type 'up' / 'down' / 'left' / 'right' and press enter. "
                         "If you wish to quit, type 'quit' and press enter: ")):
    if direction.lower() == "up":
        up()
    if direction.lower() == "down":
        down()
    if direction.lower() == "left":
        left()
    if direction.lower() == "right":
        right()
    if direction.lower() == "quit":
        gamequit()
    newrandnum()


def checkgameover():  # this checks if the player's board is full
    numbersinboard = []
    for row in board:
        for number in row:
            numbersinboard.append(number)
    if 0 not in numbersinboard:
        return True
# THIS DOES NOT WORK. IF THE PLAYER CAN STILL MAKE MOVES WHEN THE BOARD IS FULL, IT SHOULD NOT STOP THE GAME


def check2048():  # this checks if 2048 is in the board
    for row in board:
        if 2048 in row:
            return True
            break
    return False


while not check2048():  # the game-play repeats until the player gets either GAMEOVER or 2048
    show()
    move(direction=input("Please type 'up' / 'down' / 'left' / 'right' and press enter: "))
    if checkgameover():
        show()
        print("GAMEOVER")
        break

if check2048():
    show()
    print("CONGRATULATIONS! YOU WON THE GAME!")
