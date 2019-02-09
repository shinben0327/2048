"""
Created on Feb 3 2019
@author: jihwanshin
"""

import random
import sys

"""
This program recreates 2048. Notes for this project will be written here

https://en.wikipedia.org/wiki/2048_(video_game)#Gameplay

STUFF TO DO
make scoring system
rewrite  checkgameover()
make sure that rows and columns match even with big numbers
"""

print("* Hi! This is a recreation of the game 2048 on Python. Have fun! *")  # starting message
board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]  # initial starting board


def show():
    for row in board:
        print(*row)


def up():
    # this recreates the board into the column point of view
    columns = [[], [], [], []]
    for i in range(4):
        for j in range(4):
            columns[i].append(board[j][i])
    for column in columns:
        # this moves all the numbers
        counter = 0
        for i in range(3, -1, -1):
            if column[i] == 0:
                column.remove(column[i])
                counter += 1
        # this combines the numbers if they are identical
        for i in range(len(column)-1):
            if column[i] == column[i+1]:
                column[i] *= 2
                del column[i+1]
                column.append(0)
        # this makes sure that the row still has four numbers
        for i in range(counter):
            column.append(0)
    # this turns the columns back into the board
    for i in range(4):
        for j in range(4):
            board[i][j] = columns[j][i]


def down():
    # this recreates the board into the column point of view
    columns = [[], [], [], []]
    for i in range(4):
        for j in range(4):
            columns[i].append(board[j][i])
    for column in columns:
        # this moves all the numbers
        counter = 0
        for i in range(3, -1, -1):
            if column[i] == 0:
                column.remove(column[i])
                counter += 1
        # this combines the numbers if they are identical
        for i in range(len(column) - 1, 0, -1):
            if column[i] == column[i - 1]:
                column[i] *= 2
                del column[i - 1]
                column.insert(0, 0)
        # this makes sure that the row still has four numbers
        for i in range(counter):
            column.insert(0, 0)
    # this turns the columns back into the board
    for i in range(4):
        for j in range(4):
            board[i][j] = columns[j][i]


def left():
    for row in board:
        # this moves all the numbers
        counter = 0
        for i in range(3, -1, -1):
            if row[i] == 0:
                row.remove(row[i])
                counter += 1
        # this combines the numbers if they are identical
        for i in range(len(row)-1):
            if row[i] == row[i+1]:
                row[i] *= 2
                del row[i+1]
                row.append(0)
        # this makes sure that the row still has four numbers
        for i in range(counter):
            row.append(0)


def right():
    for row in board:
        # this moves all the numbers
        counter = 0
        for i in range(3, -1, -1):
            if row[i] == 0:
                row.remove(row[i])
                counter += 1
        # this combines the numbers if they are identical
        for i in range(len(row)-1, 0, -1):
            if row[i] == row[i-1]:
                row[i] *= 2
                del row[i-1]
                row.insert(0, 0)
        # this makes sure that the row still has four numbers
        for i in range(counter):
            row.insert(0, 0)


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
    twofour = random.choices(
        population=[2, 4],  # this will randomly choose the new number that will appear
        weights=[0.75, 0.25]  # 75% of the time it will be 2, 25% of the time it will be 4
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


def checkgameover():  # this checks if the player lost the game
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
    return False


while not checkgameover() and not check2048():  # the game-play repeats until the player gets either GAMEOVER or 2048
    show()
    move(direction=input("Please type 'up' / 'down' / 'left' / 'right' and press enter: "))

if checkgameover():
    show()
    print("GAMEOVER")

if check2048():
    show()
    print("CONGRATULATIONS! YOU WON THE GAME!")
