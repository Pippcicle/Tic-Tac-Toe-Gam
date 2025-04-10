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


