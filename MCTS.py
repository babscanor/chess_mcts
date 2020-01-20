import random
import copy
from game import *
from math import sqrt,log, inf

def piecerestante(board,player):
    reste=[]
    for i in range(64):
        if board.gamecases[i].pieceoncase.couleur==player:
            reste.append(i)
    return reste




