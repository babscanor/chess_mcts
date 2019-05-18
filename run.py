import pygame
from game import board
pygame.init()

green=(143,188,143)
beige=(245,222,179)


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
            if chessboard.gamecases[compteur].pieceoncase!=None:
                if chessboard.gamecases[compteur].pieceoncase.tostring()!=" ":
                    if chessboard.gamecases[compteur].pieceoncase.couleur=="Black":
                        image=pygame.image.load("chess_pieces/noirs/"+chessboard.gamecases[compteur].pieceoncase.tostring()+".png")
                    else:
                        image=pygame.image.load("chess_pieces/blancs/"+chessboard.gamecases[compteur].pieceoncase.tostring()+".png")
                    image = pygame.transform.scale(image, (80, 80))
                    fenetre.blit(image,(row,col))
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
                print(selectedpiece)
                if selectedpiece.tostring()!=" ":
                    selected=True
                print(caseactuelle)
        elif event.type==pygame.MOUSEBUTTONDOWN and selected:
            newmousex,newmousey=pygame.mouse.get_pos()
            newcaseactuelle=mousepositiontocase(newmousex,newmousey)
            print(newcaseactuelle)
            chessboard.gamecases[newcaseactuelle].pieceoncase=selectedpiece
            chessboard.reset(caseactuelle)
            selected=False
            chessboard.print_board()

    pygame.display.update()
#chessboard.print_board()

