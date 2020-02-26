bordure=[[0,8,16,24,32,40,48,56],[56,57,58,59,60,61,62,63],[0,1,2,3,4,5,6,7],[15,23,31,39,47,55,63,7],0,8,16,24,32,40,48,56,57,58,59,60,61,62,63,1,2,3,4,5,6,7,15,23,31,39,47,55]
from copy import deepcopy
from evaluation import *

class board:
    #cette classe comportera une methode player_turn qui donne le tour du joueur , une methode reset qui initialisera une case, et une methode
    # qui crée une nouvelle grille de jeu
    def __init__(self):
        self.gamecases={}
        self.compteur=0
    def reset(self, case):
        self.gamecases[case]=vide()

    def create_board(self):
        player_turn="White"
        for case in range(64):
            self.gamecases[case]=vide()
        self.gamecases[0]=tour(0,"Black")
        self.gamecases[1]=cavalier(1,"Black")
        self.gamecases[2]=eveque(2,"Black")
        self.gamecases[3]=king(3,"Black")
        self.gamecases[4]=reine(4,"Black")
        self.gamecases[5]=eveque(5,"Black")
        self.gamecases[6]=cavalier(6,"Black")
        self.gamecases[7]=tour(7,"Black")
        self.gamecases[8]=pion(8,"Black")
        self.gamecases[9]=pion(9,"Black")
        self.gamecases[10]=pion(10,"Black")
        self.gamecases[11]=pion(11,"Black")
        self.gamecases[12]=pion(12,"Black")
        self.gamecases[13]=pion(13,"Black")
        self.gamecases[14]=pion(14,"Black")
        self.gamecases[15]=pion(15,"Black")
    
        self.gamecases[63]=tour(63,"White")
        self.gamecases[62]=cavalier(62,"White")
        self.gamecases[61]=eveque(61,"White")
        self.gamecases[60]=reine(60,"White")
        self.gamecases[59]=king(59,"White")
        self.gamecases[58]=eveque(58,"White")
        self.gamecases[57]=cavalier(57,"White")
        self.gamecases[56]=tour(56,"White")
        self.gamecases[55]=pion(55,"White")
        self.gamecases[54]=pion(54,"White")
        self.gamecases[53]=pion(53,"White")
        self.gamecases[52]=pion(52,"White")
        self.gamecases[51]=pion(51,"White")
        self.gamecases[50]=pion(50,"White")
        self.gamecases[49]=pion(49,"White")
        self.gamecases[48]=pion(48,"White")

    def player_turn(self):
        if self.compteur%2==0:
            return "White"
        else:
            return "Black"

    def blackinchess(self):
        result=False
        kingslayer=None
        for case in self.gamecases:
            if self.gamecases[case].couleur=="White":
                for x in self.gamecases[case].move_possible(self):
                    if self.gamecases[x].tostring()=="K":
                        result=True
                        kingslayer=case
        return [result,kingslayer]

    def whiteinchess(self):
        result=False
        kingslayer=None
        for case in self.gamecases:
            if self.gamecases[case].couleur=="Black":
                for x in self.gamecases[case].move_possible(self):
                    if self.gamecases[x].tostring()=="k":
                        result=True
                        kingslayer=case
        return [result,kingslayer]
    def whitewin(self):
        if (self.blackinchess())[0]:
            for child in children(self, 'Black'):
                if not (child[0].blackinchess())[0]:
                    return False
            return True

    def blackwin(self):
        if (self.whiteinchess())[0]:
            for child in children(self, 'White'):
                if not (child[0].whiteinchess())[0]:
                    return False
            return True

    def final_state(self):
        if self.blackwin() or self.whitewin:
            return True
        return False


    def all_moves(self, player):
        moves = []
        for k in range(64):
            piece = self.gamecases[k]
            if piece.couleur == player:
                pos = piece.position
                moves += [(pos, target) for target in piece.move_possible(self)]
        return moves

    def print_board(self):
        compteur=0
        for case in range(64):
            print("|",end=self.gamecases[case].tostring())
            compteur+=1
            if compteur==8:
                print("|",end="\n")
                compteur=0



#les classes suivantes correspondent chacune à un type de piece, les attributs seront la position et la couleur et une methode donnera les mouvements posibles

class king:
    couleur=None
    position=None
    def __init__(self,position,couleur):
        self.position=position
        self.couleur=couleur

    def tostring(self):
        if self.couleur=="Black":
            return "K"
        else:
            return "k"
    def move_possible(self,board):
        move_possible=[]
        if self.position+8 in range(64):
            if board.gamecases[self.position+8].tostring()==" " or board.gamecases[self.position+8].couleur != board.gamecases[self.position ].couleur :
                move_possible.append(self.position+8)
        if self.position-8 in range(64):
            if board.gamecases[self.position-8].tostring()==" " or  board.gamecases[self.position-8].couleur!=board.gamecases[self.position  ].couleur:
                move_possible.append(self.position-8)
        if self.position-1 in range(64):
            if self.position not in bordure[0] and (board.gamecases[self.position-1].tostring()==" " or board.gamecases[self.position-1].couleur!=board.gamecases[self.position  ].couleur):
                move_possible.append(self.position-1)
        if self.position+1 in range(64):
            if self.position not in bordure[3] and (board.gamecases[self.position+1].tostring()==" " or board.gamecases[self.position+1].couleur!=board.gamecases[self.position  ].couleur):
                move_possible.append(self.position+1)
        if self.position+7 in range(64):
            if self.position not in bordure[0] and (board.gamecases[self.position+7].tostring()==" " or board.gamecases[self.position+7].couleur!=board.gamecases[self.position ].couleur):
                move_possible.append(self.position+7)
        if self.position-7 in range(64):
            if self.position not in bordure[3] and (board.gamecases[self.position-7].tostring()==" " or board.gamecases[self.position-7].couleur!=board.gamecases[self.position  ].couleur):
                move_possible.append(self.position-7)
        if self.position+9 in range(64):
            if self.position not in bordure[3] and (board.gamecases[self.position+9].tostring()==" " or board.gamecases[self.position+9].couleur!=board.gamecases[self.position ].couleur):
                move_possible.append(self.position+9)
        if self.position-9 in range(64):
            if self.position not in bordure[0] and (board.gamecases[self.position-9].tostring()==" " or board.gamecases[self.position-9].couleur!=board.gamecases[self.position ].couleur):
                move_possible.append(self.position-9)
        return move_possible


class reine:
    couleur=None
    position=None
    def __init__(self,position,couleur):
        self.position=position
        self.couleur=couleur
    def tostring(self):
        if self.couleur=="Black":
            return "R"
        else:
            return "r"
    def move_possible(self, board):
        pos=self.position
        move_possible=[]
        for k in range(1,(64-pos)//8 +1):
            if pos+8*k in range(0,64):
                if board.gamecases[pos+8*k].tostring()==" "  :
                    move_possible.append(pos+8*k)
                elif board.gamecases[pos+8*k].couleur!=board.gamecases[pos ].couleur :
                    move_possible.append(pos+8*k)
                    break
                elif board.gamecases[ pos+8*k  ].couleur==board.gamecases[pos ].couleur:
                    break
        for k in range(1,(pos-1)//8+2):
            if pos-8*k in range(0,64):
                if board.gamecases[pos-8*k].tostring()==" "  :
                    move_possible.append(pos-8*k)
                elif  board.gamecases[pos-8*k].couleur!=board.gamecases[pos ].couleur:
                    move_possible.append(pos-8*k)
                    break
                elif board.gamecases[ pos-8*k  ].couleur==board.gamecases[pos ].couleur:
                    break
        for k in range(1,pos-(pos//8)*8+1):
            if pos-k in range(0,64):
                if board.gamecases[pos-k].tostring()==" "  :
                    move_possible.append(pos-k)
                elif board.gamecases[pos-k].couleur!=board.gamecases[pos ].couleur:
                    move_possible.append(pos-k)
                    break
                elif board.gamecases[ pos-k  ].couleur==board.gamecases[pos ].couleur:
                    break
        for k in range(1,-pos+(pos//8 +1)*8):
            if pos+k in range(0,64):
                if board.gamecases[pos+k].tostring()==" ":
                    move_possible.append(pos+k)
                elif board.gamecases[pos+k].couleur!=board.gamecases[pos ].couleur :
                    move_possible.append(pos+k)
                    break
                elif board.gamecases[ pos+k  ].couleur==board.gamecases[pos ].couleur:
                    break
        for k in range(1,8):
            if pos+7*k in bordure and pos+7*k in range(64):
                if pos not in bordure[0]:
                    move_possible.append(pos+7*k)
                break
            elif pos+7*k in range(64):
                if board.gamecases[pos+7*k].tostring()==" "  :
                    move_possible.append(pos+7*k)
                elif board.gamecases[pos+7*k].couleur!=board.gamecases[pos ].couleur:
                    move_possible.append(pos+9*k)
                    break
                elif board.gamecases[pos+7*k ].couleur==board.gamecases[pos ].couleur:
                    break
        for k in range(1,8):
            if pos+9*k in bordure and pos+9*k in range(64) :
                if pos not in bordure[3]:
                    move_possible.append(pos+9*k)
                break
            elif pos+9*k in range(64):
                if board.gamecases[pos+9*k].tostring()==" "  :
                    move_possible.append(pos+9*k)
                elif board.gamecases[pos+9*k].couleur!=board.gamecases[pos ].couleur:
                    move_possible.append(pos+9*k)
                    break
                elif board.gamecases[pos+9*k ].couleur==board.gamecases[pos ].couleur:
                    break
        for k in range(1,8):
            if pos-7*k in bordure and pos-7*k in range(64) :
                if pos not in bordure[3]:
                    move_possible.append(pos-7*k)
                break
            elif pos-7*k in range(64):
                if board.gamecases[pos-7*k].tostring()==" "  :
                    move_possible.append(pos-7*k)
                elif  board.gamecases[pos-7*k].couleur!=board.gamecases[pos ].couleur:
                    move_possible.append(pos-7*k)
                    break
                elif board.gamecases[pos-7*k ].couleur==board.gamecases[pos ].couleur:
                    break
        for k in range(1,8):
            if pos-9*k in bordure and pos-9*k in range(64) :
                if pos not in bordure[0]:
                    move_possible.append(pos-9*k)
                break
            elif pos-9*k in range(64):
                if board.gamecases[pos-9*k].tostring()==" "  :
                    move_possible.append(pos-9*k)
                elif board.gamecases[pos-9*k].couleur!=board.gamecases[pos ].couleur:
                    move_possible.append(pos-9*k)
                    break
                elif board.gamecases[pos-9*k ].couleur==board.gamecases[pos ].couleur:
                    break
        return move_possible

class eveque:
    couleur=None
    position=None
    def __init__(self,position,couleur):
        self.position=position
        self.couleur=couleur
    def tostring(self):
        if self.couleur=="Black":
            return "E"
        else:
            return "e"
    def move_possible(self, board):
        pos=self.position
        move_possible=[]
        for k in range(1,8):
            if pos+7*k in bordure and pos+7*k in range(64):
                if pos not in bordure[0]:
                    move_possible.append(pos+7*k)
                break
            elif pos+7*k in range(64):
                if board.gamecases[pos+7*k].tostring()==" "  :
                    move_possible.append(pos+7*k)
                elif board.gamecases[pos+7*k].couleur!=board.gamecases[pos ].couleur:
                    move_possible.append(pos+9*k)
                    break
                elif board.gamecases[pos+7*k ].couleur==board.gamecases[pos ].couleur:
                    break
        for k in range(1,8):
            if pos+9*k in bordure and pos+9*k in range(64) :
                if pos not in bordure[3]:
                    move_possible.append(pos+9*k)
                break
            elif pos+9*k in range(64):
                if board.gamecases[pos+9*k].tostring()==" "  :
                    move_possible.append(pos+9*k)
                elif board.gamecases[pos+9*k].couleur!=board.gamecases[pos ].couleur:
                    move_possible.append(pos+9*k)
                    break
                elif board.gamecases[pos+9*k ].couleur==board.gamecases[pos ].couleur:
                    break
        for k in range(1,8):
            if pos-7*k in bordure and pos-7*k in range(64) :
                if pos not in bordure[3]:
                    move_possible.append(pos-7*k)
                break
            elif pos-7*k in range(64):
                if board.gamecases[pos-7*k].tostring()==" "  :
                    move_possible.append(pos-7*k)
                elif  board.gamecases[pos-7*k].couleur!=board.gamecases[pos ].couleur:
                    move_possible.append(pos-7*k)
                    break
                elif board.gamecases[pos-7*k ].couleur==board.gamecases[pos ].couleur:
                    break
        for k in range(1,8):
            if pos-9*k in bordure and pos-9*k in range(64) :
                if pos not in bordure[0]:
                    move_possible.append(pos-9*k)
                break
            elif pos-9*k in range(64):
                if board.gamecases[pos-9*k].tostring()==" "  :
                    move_possible.append(pos-9*k)
                elif board.gamecases[pos-9*k].couleur!=board.gamecases[pos ].couleur:
                    move_possible.append(pos-9*k)
                    break
                elif board.gamecases[pos-9*k ].couleur==board.gamecases[pos ].couleur:
                    break
        return move_possible

class tour:
    couleur=None
    position=None
    def __init__(self,position,couleur):
        self.position=position
        self.couleur=couleur
    def tostring(self):
        if self.couleur=="Black":
            return "T"
        else:
            return "t"
    def move_possible(self,board):
        pos=self.position
        move_possible=[]
        for k in range(1,(64-pos)//8 +1):
            if pos+8*k in range(0,64):
                if board.gamecases[pos+8*k].tostring()==" "  :
                    move_possible.append(pos+8*k)
                elif board.gamecases[pos+8*k].couleur!=board.gamecases[pos ].couleur :
                    move_possible.append(pos+8*k)
                    break
                elif board.gamecases[ pos+8*k  ].couleur==board.gamecases[pos ].couleur:
                    break
        for k in range(1,(pos-1)//8+2):
            if pos-8*k in range(0,64):
                if board.gamecases[pos-8*k].tostring()==" "  :
                    move_possible.append(pos-8*k)
                elif  board.gamecases[pos-8*k].couleur!=board.gamecases[pos ].couleur:
                    move_possible.append(pos-8*k)
                    break
                elif board.gamecases[ pos-8*k  ].couleur==board.gamecases[pos ].couleur:
                    break
        for k in range(1,pos-(pos//8)*8+1):
            if pos-k in range(0,64):
                if board.gamecases[pos-k].tostring()==" "  :
                    move_possible.append(pos-k)
                elif board.gamecases[pos-k].couleur!=board.gamecases[pos ].couleur:
                    move_possible.append(pos-k)
                    break
                elif board.gamecases[ pos-k  ].couleur==board.gamecases[pos ].couleur:
                    break
        for k in range(1,-pos+(pos//8 +1)*8):
            if pos+k in range(0,64):
                if board.gamecases[pos+k].tostring()==" ":
                    move_possible.append(pos+k)
                elif board.gamecases[pos+k].couleur!=board.gamecases[pos ].couleur :
                    move_possible.append(pos+k)
                    break
                elif board.gamecases[ pos+k  ].couleur==board.gamecases[pos ].couleur:
                    break
        return move_possible

class cavalier:
    couleur=None
    position=None
    def __init__(self,position,couleur):
        self.position=position
        self.couleur=couleur
    def tostring(self):
        if self.couleur=="Black":
            return "C"
        else:
            return "c"
    def move_possible(self,board):
        move_possible=[]
        pos=self.position
        if pos+10 in range(64) :
            if board.gamecases[pos+10].tostring()==" "  or board.gamecases[pos+10 ].couleur!=board.gamecases[pos].couleur:
                if pos%8<=5:
                    move_possible.append(pos+10)
        if pos-6 in range(64):
            if board.gamecases[pos-6].tostring()==" "  or board.gamecases[ pos-6 ].couleur!=board.gamecases[pos ].couleur:
                if pos%8<=5:
                    move_possible.append(pos-6)
        if pos+6 in range(64):
            if  board.gamecases[pos+6].tostring()==" "  or board.gamecases[ pos+6 ].couleur!=board.gamecases[pos ].couleur:
                if pos%8>=2:
                    move_possible.append(pos+6)
        if pos-10 in range(64):
            if board.gamecases[pos-10].tostring()==" " or board.gamecases[ pos-10 ].couleur!=board.gamecases[pos ].couleur:
                if pos%8>=2:
                    move_possible.append(pos-10)
        if pos+17 in range(64):
            if board.gamecases[pos+17].tostring()==" " or board.gamecases[ pos+17 ].couleur!=board.gamecases[pos ].couleur:
                if pos%8<7:
                    move_possible.append(pos+17)
        if pos+15 in range(64):
            if board.gamecases[pos+15].tostring()==" " or board.gamecases[ pos+15].couleur!=board.gamecases[pos ].couleur:
                if pos%8>0:
                    move_possible.append(pos+15)
        if pos-15 in range(64):
            if  board.gamecases[pos-15].tostring()==" " or board.gamecases[ pos-15 ].couleur!=board.gamecases[pos ].couleur:
                if  pos%8<7:
                    move_possible.append(pos-15)
        if pos-17 in range(64):
            if board.gamecases[pos-17].tostring()==" " or board.gamecases[ pos-17 ].couleur!=board.gamecases[pos ].couleur:
                if pos%8>0:
                    move_possible.append(pos-17)
        return move_possible


class pion:
    couleur=None
    position=None
    def __init__(self,position,couleur):
        self.position=position
        self.couleur=couleur
    def tostring(self):
        if self.couleur=="Black":
            return "P"
        else:
            return "p"
    def move_possible(self,board):
        move_possible=[]
        pos=self.position
        if self.couleur=="Black":
            for k in (1,2):
                if pos+k*8 in range(64):
                    if board.gamecases[pos+8*k].tostring()==" "  :
                        move_possible.append(pos+k*8)
                    else:
                        break
            if self.position+9 in range(64) and board.gamecases[self.position+9].couleur=="White":
                if self.position not in bordure[3]:
                    move_possible.append(self.position+9)
            if self.position+7 in range(64) and board.gamecases[self.position+7].couleur=="White":
                if self.position not in bordure[0]:
                    move_possible.append(self.position+7)
        else:
            for k in (1,2):
                if pos-k*8 in range(64):
                    if board.gamecases[pos-8*k].tostring()==" "  :
                        move_possible.append(pos-k*8)
                    else:
                        break
            if self.position-7 in range(64) and board.gamecases[self.position-7].couleur=="Black":
                if self.position not in bordure[3]:
                    move_possible.append(self.position-7)
            if self.position-9 in range(64) and board.gamecases[self.position-9].couleur=="Black":
                if self.position not in bordure[0]:
                    move_possible.append(self.position-9)
        return move_possible


class vide:
    couleur="green"
    targeted=False
    def __init__(self):
        pass
    def tostring(self):
        return " "

def move(chessboard, past, future):
    chessboard.gamecases[future] = chessboard.gamecases[past]
    chessboard.reset(past) 
    chessboard.gamecases[future].position =future
    chessboard.compteur += 1

def copy_board(chessboard):
    new_board = board()
    new_board.compteur =chessboard.compteur
    new_board.gamecases = deepcopy(chessboard.gamecases)
    return new_board

def children(chessboard, player):
    children = []
    for case in range(64):
        piece = chessboard.gamecases[case]
        if piece.couleur == player:
            position = chessboard.gamecases[case].position
            for mouvement in piece.move_possible(chessboard):
                child = copy_board(chessboard)
                move(child,position, mouvement)
                children.append((child,position, mouvement))
    return children

# A= board()
# A.create_board()
# print(evaluation_square_table_white(A))

# for child in children(A, 'Black'):
#     print(child[0])
#     child[0].print_board()
# A.print_board()