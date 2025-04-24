#importing the libraries
import tkinter
from tkinter import *
from tkinter import messagebox
import random
from functools import partial
from copy import deepcopy

#variable decide the turn of the player
sign = 0

#create an empty board
global board
board = [["" for x in range(3)] for y in range(3)]

#check who wins the match based on rules of the game
def winner(b,l): 
    return( (b[0][0] == l and b[0][1] == l and b[0][2] == l) or 
           (b[1][0] == l and b[1][1] == l and b[1][2] == l) or 
           (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
           (b[0][0] == l and b[1][0] == l and b[2][0] == l) or 
           (b[0][1] == l and b[1][1] == l and b[2][1] == l) or 
           (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
           (b[0][0] == l and b[1][1] == l and b[2][2] == l) or 
           (b[0][2] == l and b[1][1] == l and b[2][0] == l)
           )

#configure text on button while playing with another player
def get_text(i, j, l1, l2, gb): 
    global sign, board
    if board[i][j] == " ":
        if sign % 2 == 0 : 
            l1.config(state = DISABLED)
            l2.config(state = ACTIVE)
            board[i][j] = "X"
        else : 
            l1.config(state = ACTIVE)
            l2.config(state = DISABLED)
            board[i][j] = "O"
        sign += 1 
        button[i][j].config(text = board[i][j])
    if winner(board,"X"): 
        gb.destroy()
        box = messagebox.showinfo("Winner","Player 1 is the winner")
    elif winner(board, "O"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 2 is the winner")
    else : 
        gb.destroy()
        box = messagebox.showinfo("Tie", "The game is a tie")

def isfull():
    flag = True
    for i in board : 
        if (i.count(" ") > 0 ): 
            flag = False
    return flag




