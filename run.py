import pygame
from game import board
pygame.init()

#initialize some colors
green=(143,188,143)
beige=(245,222,179)
font = pygame.font.Font('freesansbold.ttf', 32)
bchess = font.render('Black in chess', True, (0,0,0))
wchess = font.render('White in chess', True,  (0,0,0))
bwin = font.render('Black wins', True,  (0,0,0))
wwin = font.render('White wins', True, (0,0,0))
pos_up=[275,700]
pos_down=[275,20]

#chreating a new pygame window and printing an initilize board game
fenetre=pygame.display.set_mode((750,750))
couleur_fenetre=[220,220,220]
pygame.display.set_caption("Chess")
chessboard=board()
chessboard.create_board()
chessboard.print_board()

def draw_case(x,y,size,color):
    # trace un rectangle de position, largeur et longueur données
    pygame.draw.rect(fenetre,color,(x,y,size,size))



def update_board():
    # actualise la fenetre de jeu à chaque itération, affiche les pieces deplacées etc
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

def message(text,color,pos):
    screen_text=font.render(text, True, color)
    fenetre.blit(screen_text,pos)

def mousepositiontocase(x,y):
    #prend des coordonnées sur l'écran et indique la case à laquelle ça correspond
    compteur=0
    for j in [55+k*80 for k in range(8)]:
        for i in [55+k*80 for k in range(8)]:
            if i<x<i+80 and j<y<j+80 :
                return compteur
            compteur+=1


selected=False
quitgame=False

while not quitgame:
    #à chaque itération, on réaffiche la fenetre actualisée
    moved=False
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
    #print(chessboard.player_turn())
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and not selected:
            # si la souris est cliquée, on vérifie que la case cliquée est non vide, puis on vend True la variable booléenne selected, on affiche les mouvements possibles pout cette case
            mousex,mousey=pygame.mouse.get_pos()
            if chessboard.gamecases[mousepositiontocase(mousex,mousey)].pieceoncase.tostring()!=" ":
                caseactuelle=mousepositiontocase(mousex,mousey)
                selectedpiece=chessboard.gamecases[caseactuelle].pieceoncase
                #print(selectedpiece)
                if selectedpiece.tostring()!=" ":
                    selected=True
                move_possibles=selectedpiece.move_possible(chessboard)
                print(move_possibles)
                for case in move_possibles:
                    chessboard.gamecases[case].pieceoncase.targeted=True

                print(caseactuelle)


        elif event.type==pygame.MOUSEBUTTONDOWN and selected:
            # si une case est selectionnée, et qu'on clique dans une nouvelle case et que le mouvement est valide, on fait le mouvement
            newmousex,newmousey=pygame.mouse.get_pos()
            newcaseactuelle=mousepositiontocase(newmousex,newmousey)
            if newcaseactuelle in move_possibles:
                print(newcaseactuelle)
                chessboard.gamecases[newcaseactuelle].pieceoncase=selectedpiece
                chessboard.gamecases[newcaseactuelle].pieceoncase.position=newcaseactuelle
                chessboard.reset(caseactuelle)
                moved=True
            selected=False
            #print(chessboard.player_turn())
            if moved==True:
                chessboard.compteur+=1
            if not selected:
                for case in move_possibles:
                    chessboard.gamecases[case].pieceoncase.targeted=False
            #chessboard.print_board()
            #print(chessboard.player_turn())
            #print(chessboard.blackinchess()[0],chessboard.whitewin())
    #on vérifie s'il y'a des joueurs en echecs
    if chessboard.blackinchess()[0]:
        message("black in chess",(34, 167, 240),pos_down)
    if chessboard.whiteinchess()[0]:
        message("white in chess",(34, 167, 240),pos_down)
    if chessboard.blackwin():
        message("black wins",(255,0,0),pos_up)
    if chessboard.whitewin():
        message("white wins",(255,0,0),pos_up)
    pygame.display.update()


