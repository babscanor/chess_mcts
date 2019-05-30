bordure=[[0,8,16,24,32,40,48,56],[56,57,58,59,60,61,62,63],[0,1,2,3,4,5,6,7],[15,23,31,39,47,55,63],0,8,16,24,32,40,48,56,57,58,59,60,61,62,63,1,2,3,4,5,6,7,15,23,31,39,47,55]

class board:
    gamecases={}
    def __init__(self):
        pass
    def reset(self, case):
        self.gamecases[case]=cases(case,vide())
    def create_board(self):
        for case in range(64):
            self.gamecases[case]=cases(case,vide())

        self.gamecases[0]=cases(0,tour(0,"Black"))
        self.gamecases[1]=cases(1,cavalier(1,"Black"))
        self.gamecases[2]=cases(2,eveque(2,"Black"))
        self.gamecases[3]=cases(3,king(3,"Black"))
        self.gamecases[4]=cases(4,reine(4,"Black"))
        self.gamecases[5]=cases(5,eveque(5,"Black"))
        self.gamecases[6]=cases(6,cavalier(6,"Black"))
        self.gamecases[7]=cases(7,tour(7,"Black"))
        self.gamecases[8]=cases(8,pion(8,"Black"))
        self.gamecases[9]=cases(9,pion(9,"Black"))
        self.gamecases[10]=cases(10,pion(10,"Black"))
        self.gamecases[11]=cases(11,pion(11,"Black"))
        self.gamecases[12]=cases(12,pion(12,"Black"))
        self.gamecases[13]=cases(13,pion(13,"Black"))
        self.gamecases[14]=cases(14,pion(14,"Black"))
        self.gamecases[15]=cases(15,pion(15,"Black"))

        self.gamecases[63]=cases(63,tour(63,"White"))
        self.gamecases[62]=cases(62,cavalier(62,"White"))
        self.gamecases[61]=cases(61,eveque(61,"White"))
        self.gamecases[60]=cases(60,reine(60,"White"))
        self.gamecases[59]=cases(59,king(59,"White"))
        self.gamecases[58]=cases(58,eveque(58,"White"))
        self.gamecases[57]=cases(57,cavalier(57,"White"))
        self.gamecases[56]=cases(56,tour(56,"White"))
        self.gamecases[55]=cases(55,pion(55,"White"))
        self.gamecases[54]=cases(54,pion(54,"White"))
        self.gamecases[53]=cases(53,pion(53,"White"))
        self.gamecases[52]=cases(52,pion(52,"White"))
        self.gamecases[51]=cases(51,pion(51,"White"))
        self.gamecases[50]=cases(50,pion(50,"White"))
        self.gamecases[49]=cases(49,pion(49,"White"))
        self.gamecases[48]=cases(48,pion(48,"White"))
    def blackinchess(self):
        result=False
        kingslayer=None
        for case in self.gamecases:
            if self.gamecases[case].pieceoncase.couleur=="White":
                for x in self.gamecases[case].pieceoncase.move_possible(self):
                    if self.gamecases[x].pieceoncase.tostring()=="K":
                        result=True
                        kingslayer=case
        return [result,kingslayer]
    def whiteinchess(self):
        result=False
        kingslayer=None
        for case in self.gamecases:
            if self.gamecases[case].pieceoncase.couleur=="Black":
                for x in self.gamecases[case].pieceoncase.move_possible(self):
                    if self.gamecases[x].pieceoncase.tostring()=="k":
                        result=True
                        kingslayer=case
        return [result,kingslayer]
    def whitewin(self):
        result=False
        if self.blackinchess()[0]:
            for case in self.gamecases:
                if self.gamecases[case].pieceoncase.tostring()=="K":
                    result=True
                    for x in self.gamecases[case].pieceoncase.move_possible(self):
                        if x in self.gamecases[self.blackinchess()[1]].pieceoncase.move_possible(self):
                            result=True
        return result

    def blackwinwin(self):
        result=False
        if self.whiteinchess()[0]:
            for case in self.gamecases:
                if self.gamecases[case].pieceoncase.tostring()=="K":
                    result=True
                    for x in self.gamecases[case].pieceoncase.move_possible():
                        if x in self.gamecases[self.whiteinchess()[1]].pieceoncase.move_possible():
                            result=True
        return result

    def print_board(self):
        compteur=0
        for case in range(64):
            print("|",end=self.gamecases[case].pieceoncase.tostring())
            compteur+=1
            if compteur==8:
                print("|",end="\n")
                compteur=0


class cases:
    pieceoncase=None
    coordonnee=None
    def __init__(self,coordonnee,piece):
        self.coordonnee=coordonnee
        self.pieceoncase=piece


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
            if board.gamecases[self.position+8].pieceoncase.tostring()==" " or board.gamecases[self.position+8].pieceoncase.couleur != board.gamecases[self.position ].pieceoncase.couleur :
                move_possible.append(self.position+8)
        if self.position-8 in range(64):
            if board.gamecases[self.position-8].pieceoncase.tostring()==" " or  board.gamecases[self.position-8].pieceoncase.couleur!=board.gamecases[self.position  ].pieceoncase.couleur:
                move_possible.append(self.position-8)
        if self.position-1 in range(64):
            if board.gamecases[self.position-1].pieceoncase.tostring()==" " or board.gamecases[self.position-1].pieceoncase.couleur!=board.gamecases[self.position  ].pieceoncase.couleur:
                move_possible.append(self.position-1)
        if self.position+1 in range(64):
            if board.gamecases[self.position+1].pieceoncase.tostring()==" " or board.gamecases[self.position+1].pieceoncase.couleur!=board.gamecases[self.position  ].pieceoncase.couleur:
                move_possible.append(self.position+1)
        if self.position+7 in range(64):
            if board.gamecases[self.position+7].pieceoncase.tostring()==" " or board.gamecases[self.position+7].pieceoncase.couleur!=board.gamecases[self.position ].pieceoncase.couleur:
                move_possible.append(self.position+7)
        if self.position-7 in range(64):
            if board.gamecases[self.position-7].pieceoncase.tostring()==" " or board.gamecases[self.position-7].pieceoncase.couleur!=board.gamecases[self.position  ].pieceoncase.couleur:
                move_possible.append(self.position-7)
        if self.position+9 in range(64):
            if board.gamecases[self.position+9].pieceoncase.tostring()==" " or board.gamecases[self.position+9].pieceoncase.couleur!=board.gamecases[self.position ].pieceoncase.couleur:
                move_possible.append(self.position+9)
        if self.position-9 in range(64):
            if board.gamecases[self.position-9].pieceoncase.tostring()==" " or board.gamecases[self.position-9].pieceoncase.couleur!=board.gamecases[self.position ].pieceoncase.couleur:
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
            if pos+8*k in range(1,64):
                if board.gamecases[pos+8*k].pieceoncase.tostring()==" "  :
                    move_possible.append(pos+8*k)
                elif board.gamecases[pos+8*k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur :
                    move_possible.append(pos+8*k)
                    break
                elif board.gamecases[ pos+8*k  ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
                    break
        for k in range(1,(pos-1)//8+1):
            if pos-8*k in range(1,64):
                if board.gamecases[pos-8*k].pieceoncase.tostring()==" "  :
                    move_possible.append(pos-8*k)
                elif  board.gamecases[pos-8*k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                    move_possible.append(pos-8*k)
                    break
                elif board.gamecases[ pos-8*k  ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
                    break
        for k in range(1,pos-(pos//8)*8+1):
            if pos-k in range(0,64):
                if board.gamecases[pos-k].pieceoncase.tostring()==" "  :
                    move_possible.append(pos-k)
                elif board.gamecases[pos-k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                    move_possible.append(pos-k)
                    break
                elif board.gamecases[ pos-k  ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
                    break
        for k in range(1,-pos+(pos//8 +1)*8):
            if pos+k in range(1,64):
                if board.gamecases[pos+k].pieceoncase.tostring()==" ":
                    move_possible.append(pos+k)
                elif board.gamecases[pos+k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur :
                    move_possible.append(pos+k)
                    break
                elif board.gamecases[ pos+k  ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
                    break
        for k in range(1,8):
            if pos+7*k in bordure and pos+7*k in range(64):
                if pos not in bordure[0]:
                    move_possible.append(pos+7*k)
                break
            elif pos+7*k in range(64):
                if board.gamecases[pos+7*k].pieceoncase.tostring()==" "  :
                    move_possible.append(pos+7*k)
                elif board.gamecases[pos+7*k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                    move_possible.append(pos+9*k)
                    break
                elif board.gamecases[pos+7*k ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
                    break
        for k in range(1,8):
            if pos+9*k in bordure and pos+9*k in range(64) :
                if pos not in bordure[3]:
                    move_possible.append(pos+9*k)
                break
            elif pos+9*k in range(64):
                if board.gamecases[pos+9*k].pieceoncase.tostring()==" "  :
                    move_possible.append(pos+9*k)
                elif board.gamecases[pos+9*k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                    move_possible.append(pos+9*k)
                    break
                elif board.gamecases[pos+9*k ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
                    break
        for k in range(1,8):
            if pos-7*k in bordure and pos-7*k in range(64) :
                if pos not in bordure[3]:
                    move_possible.append(pos-7*k)
                break
            elif pos-7*k in range(64):
                if board.gamecases[pos-7*k].pieceoncase.tostring()==" "  :
                    move_possible.append(pos-7*k)
                elif  board.gamecases[pos-7*k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                    move_possible.append(pos-7*k)
                    break
                elif board.gamecases[pos-7*k ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
                    break
        for k in range(1,8):
            if pos-9*k in bordure and pos-9*k in range(64) :
                if pos not in bordure[0]:
                    move_possible.append(pos-9*k)
                break
            elif pos-9*k in range(64):
                if board.gamecases[pos-9*k].pieceoncase.tostring()==" "  :
                    move_possible.append(pos-9*k)
                elif board.gamecases[pos-9*k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                    move_possible.append(pos-9*k)
                    break
                elif board.gamecases[pos-9*k ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
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
                if board.gamecases[pos+7*k].pieceoncase.tostring()==" "  :
                    move_possible.append(pos+7*k)
                elif board.gamecases[pos+7*k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                    move_possible.append(pos+9*k)
                    break
                elif board.gamecases[pos+7*k ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
                    break
        for k in range(1,8):
            if pos+9*k in bordure and pos+9*k in range(64) :
                if pos not in bordure[3]:
                    move_possible.append(pos+9*k)
                break
            elif pos+9*k in range(64):
                if board.gamecases[pos+9*k].pieceoncase.tostring()==" "  :
                    move_possible.append(pos+9*k)
                elif board.gamecases[pos+9*k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                    move_possible.append(pos+9*k)
                    break
                elif board.gamecases[pos+9*k ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
                    break
        for k in range(1,8):
            if pos-7*k in bordure and pos-7*k in range(64) :
                if pos not in bordure[3]:
                    move_possible.append(pos-7*k)
                break
            elif pos-7*k in range(64):
                if board.gamecases[pos-7*k].pieceoncase.tostring()==" "  :
                    move_possible.append(pos-7*k)
                elif  board.gamecases[pos-7*k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                    move_possible.append(pos-7*k)
                    break
                elif board.gamecases[pos-7*k ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
                    break
        for k in range(1,8):
            if pos-9*k in bordure and pos-9*k in range(64) :
                if pos not in bordure[0]:
                    move_possible.append(pos-9*k)
                break
            elif pos-9*k in range(64):
                if board.gamecases[pos-9*k].pieceoncase.tostring()==" "  :
                    move_possible.append(pos-9*k)
                elif board.gamecases[pos-9*k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                    move_possible.append(pos-9*k)
                    break
                elif board.gamecases[pos-9*k ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
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
            if pos+8*k in range(1,64):
                if board.gamecases[pos+8*k].pieceoncase.tostring()==" "  :
                    move_possible.append(pos+8*k)
                elif board.gamecases[pos+8*k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur :
                    move_possible.append(pos+8*k)
                    break
                elif board.gamecases[ pos+8*k  ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
                    break
        for k in range(1,(pos-1)//8+1):
            if pos-8*k in range(1,64):
                if board.gamecases[pos-8*k].pieceoncase.tostring()==" "  :
                    move_possible.append(pos-8*k)
                elif  board.gamecases[pos-8*k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                    move_possible.append(pos-8*k)
                    break
                elif board.gamecases[ pos-8*k  ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
                    break
        for k in range(1,pos-(pos//8)*8+1):
            if pos-k in range(0,64):
                if board.gamecases[pos-k].pieceoncase.tostring()==" "  :
                    move_possible.append(pos-k)
                elif board.gamecases[pos-k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                    move_possible.append(pos-k)
                    break
                elif board.gamecases[ pos-k  ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
                    break
        for k in range(1,-pos+(pos//8 +1)*8):
            if pos+k in range(1,64):
                if board.gamecases[pos+k].pieceoncase.tostring()==" ":
                    move_possible.append(pos+k)
                elif board.gamecases[pos+k].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur :
                    move_possible.append(pos+k)
                    break
                elif board.gamecases[ pos+k  ].pieceoncase.couleur==board.gamecases[pos ].pieceoncase.couleur:
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
            if board.gamecases[pos+10].pieceoncase.tostring()==" "  or board.gamecases[pos+10 ].pieceoncase.couleur!=board.gamecases[pos].pieceoncase.couleur:
                if pos%8<=5:
                    move_possible.append(pos+10)
        if pos-6 in range(64):
            if board.gamecases[pos-6].pieceoncase.tostring()==" "  or board.gamecases[ pos-6 ].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                if pos%8<=5:
                    move_possible.append(pos-6)
        if pos+6 in range(64):
            if  board.gamecases[pos+6].pieceoncase.tostring()==" "  or board.gamecases[ pos+6 ].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                if pos%8>=2:
                    move_possible.append(pos+6)
        if pos-10 in range(64):
            if board.gamecases[pos-10].pieceoncase.tostring()==" " or board.gamecases[ pos-10 ].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                if pos%8>=2:
                    move_possible.append(pos-10)
        if pos+17 in range(64):
            if board.gamecases[pos+17].pieceoncase.tostring()==" " or board.gamecases[ pos+17 ].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                if pos%8<7:
                    move_possible.append(pos+17)
        if pos+15 in range(64):
            if board.gamecases[pos+15].pieceoncase.tostring()==" " or board.gamecases[ pos+15].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                if pos%8>0:
                    move_possible.append(pos+15)
        if pos-15 in range(64):
            if  board.gamecases[pos-15].pieceoncase.tostring()==" " or board.gamecases[ pos-15 ].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
                if  pos%8<7:
                    move_possible.append(pos-15)
        if pos-17 in range(64):
            if board.gamecases[pos-17].pieceoncase.tostring()==" " or board.gamecases[ pos-17 ].pieceoncase.couleur!=board.gamecases[pos ].pieceoncase.couleur:
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
        if self.couleur=="Black":
            if self.position+8 in range(64) :
                move_possible.append(self.position+8)
            if self.position+16 in range(64):
                move_possible.append(self.position+16)
        else:
            if self.position-8 in range(64) :
                move_possible.append(self.position-8)
            if self.position-16 in range(64):
                move_possible.append(self.position-16)
        return move_possible


class vide:
    couleur="green"
    targeted=False
    def __init__(self):
        pass
    def tostring(self):
        return " "


