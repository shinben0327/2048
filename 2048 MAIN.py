"""
Created on Feb 3 2019
@author: jihwanshin
"""

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

board = [[0, 0, 0, 2], [0, 0, 4, 0], [0, 0, 2, 0], [0, 4, 0, 0]]

def show():
    for row in board:
        print(*row)

def up():
    pass
def down():
    pass
def left(): #it can now move rows with ONE number
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
    #make a number appear at random place 75% 2 and 25% 4
    if direction == "up":
        up()
    if direction == "down":
        down()
    if direction == "left":
        left()
    if direction == "right":
        right()

left()
show()