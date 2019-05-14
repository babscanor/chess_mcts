class board:
    gamecases={}
    def __init__(self):
        pass
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

class fou:
    couleur=None
    position=None
    def __init__(self,position,couleur):
        self.position=position
        self.couleur=couleur

    def tostring(self):
        if self.couleur=="Black":
            return "F"
        else:
            return "f"

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

class vide:
    def __init__(self):
        pass
    def tostring(self):
        return " "
