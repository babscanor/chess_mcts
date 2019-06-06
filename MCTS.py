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



def children(board):
    player=board.player_turn()
    children=[]
    for piece in piecerestante(board,player):
        moves=board.gamecases[piece].pieceoncase.move_possible(board)
        print(moves)
        for move in moves:
            newboard=copy_board(board)
            newboard.gamecases[move].pieceoncase=board.gamecases[piece].pieceoncase
            newboard.gamecases[move].pieceoncase.position=move
            newboard.reset(piece)
            children.append(newboard)
    return children
