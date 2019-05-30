import pygame
from game import board
pygame.init()

green=(143,188,143)
beige=(245,222,179)

font = pygame.font.Font('freesansbold.ttf', 32)
bchess = font.render('Black in chess', True, (0,0,0))
wchess = font.render('White in chess', True,  (0,0,0))
bwin = font.render('Black wins', True,  (0,0,0))
wwin = font.render('White wins', True, (0,0,0))

fenetre=pygame.display.set_mode((750,750))
couleur_fenetre=[220,220,220]
pygame.display.set_caption("Chess")

chessboard=board()
chessboard.create_board()
chessboard.print_board()

def draw_case(x,y,size,color):
    pygame.draw.rect(fenetre,color,(x,y,size,size))



def update_board():
    row=55
    col=55
    compteur=0
    size=80
    for x in range(8):
        for y in range(8):
            #if chessboard.gamecases[compteur].pieceoncase!=None:
            if chessboard.gamecases[compteur].pieceoncase.tostring()!=" ":
                if chessboard.gamecases[compteur].pieceoncase.couleur=="Black":
                    image=pygame.image.load("chess_pieces/noirs/"+chessboard.gamecases[compteur].pieceoncase.tostring()+".png")
                else:
                    image=pygame.image.load("chess_pieces/blancs/"+chessboard.gamecases[compteur].pieceoncase.tostring()+".png")
                image = pygame.transform.scale(image, (80, 80))
                fenetre.blit(image,(row,col))
            elif chessboard.gamecases[compteur].pieceoncase.tostring()==" ":
                if chessboard.gamecases[compteur].pieceoncase.targeted==True:
                    image=pygame.image.load("chess_pieces/blackdot.png")
                    image=pygame.transform.scale(image, (30,30))
                    fenetre.blit(image,(row+25,col+25))
            row+=size
            compteur+=1
        row=55
        col+=size

def mousepositiontocase(x,y):
    compteur=0
    for j in [55+k*80 for k in range(8)]:
        for i in [55+k*80 for k in range(8)]:
            if i<x<i+80 and j<y<j+80 :
                return compteur
            compteur+=1


selected=False
quitgame=False
while not quitgame:
    fenetre.fill(couleur_fenetre)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quitgame=True
            pygame.quit()
            quit()

    z=0
    size=80
    row=55
    col=55
    for x in range(8):
        for y in range(8):
            if z%2==0:
                draw_case(row,col,size,beige)
            else:
                draw_case(row,col,size,green)
            row+=size
            z+=1
        row=55
        z+=-1
        col+=size
    update_board()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and not selected:
            mousex,mousey=pygame.mouse.get_pos()
            if chessboard.gamecases[mousepositiontocase(mousex,mousey)].pieceoncase.tostring()!=" ":
                caseactuelle=mousepositiontocase(mousex,mousey)
                selectedpiece=chessboard.gamecases[caseactuelle].pieceoncase
                #print(selectedpiece)
                if selectedpiece.tostring()!=" ":
                    selected=True
                move_possibles=selectedpiece.move_possible(chessboard)
                for case in move_possibles:
                    chessboard.gamecases[case].pieceoncase.targeted=True

                #print(caseactuelle)


        elif event.type==pygame.MOUSEBUTTONDOWN and selected:
            newmousex,newmousey=pygame.mouse.get_pos()
            newcaseactuelle=mousepositiontocase(newmousex,newmousey)
            if newcaseactuelle in move_possibles:
                #print(newcaseactuelle)
                chessboard.gamecases[newcaseactuelle].pieceoncase=selectedpiece
                chessboard.gamecases[newcaseactuelle].pieceoncase.position=newcaseactuelle
                chessboard.reset(caseactuelle)
            selected=False
            if not selected:
                for case in move_possibles:
                    chessboard.gamecases[case].pieceoncase.targeted=False
            #chessboard.print_board()

            #print(chessboard.blackinchess()[0],chessboard.whitewin())
    if chessboard.blackinchess()[0]:
        text=bchess
        textRect = text.get_rect()
        textRect.center = ((717,5), 375)
        fenetre.blit(text, textRect)
    if chessboard.whitewin():
        text=wwin
        textRect = text.get_rect()
        textRect.center = ((717,5), 375)
        fenetre.blit(text, textRect)

    pygame.display.update()


