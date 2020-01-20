def evaluation_points_white(board):
    '''

    :param board:
    :return: le nombre de points (blanc, noir) en fonction des pièces présentent sur le terrain
    Chaque pièce a un nombre de points exprimé en centipion (1 centième de pion)
    '''
    points = {"R":900, "r":900,"E":330, "e":330, "T":500,"t":500, "C":320,"c":320,"P":100,"p":100}
    black = 0
    white =0
    for piece in board.gamecases:
        if board.gamecases[piece] != None:
           if board.gamecases[piece].couleur == "White":
               if board.gamecases[piece].tostring() != "k":
                    white += points[board.gamecases[piece].tostring()]
           if board.gamecases[piece].couleur == "Black":
               if board.gamecases[piece].tostring() != "K":
                    black += points[board.gamecases[piece].tostring()]
    if board.whitewins():
        white = 3000
    if board.blackwins():
       black = 3000
    return (white,black)

def mobility(board,couleur):
    '''
    :param board:
    :param couleur:
    :return: Le nombre de coups possibles pour le joueur "couleur"
    '''
    mobility =0
    for piece in board:
        if board.gamecases[piece].couleur == couleur:
            mobility += len(board.gamecases[piece].movepossible)
    return mobility


def end_game(board):
    '''
    :param board:
    :return: Si l'on est plutôt ver sle début de la partie ou la fin
    Se base sur le nombre de points encore présent sur l'échiquier (4000 points au total au début)
    '''
    points = {"R":900, "r":900,"E":330, "e":330, "T":500,"t":500, "C":320,"c":320,"P":100,"p":100}
    points_on_board =0
    for piece in board.gamecases:
        if board.gamecases[piece] != None:
               if board.gamecases[piece].tostring() != "k":
                    if board.gamecases[piece].tostring() != "K":
                        points_on_board += points[board.gamecases[piece].tostring()]
    if points_on_board < 2000:
        return True
    return False




def evaluation_square_table_white(board):
    '''
    Selon la position de chaque pièce sur l'échiquier on lui attribue des points
    :param board:
    :return: le nombre de points pour (blanc,noir)
    '''
    white_score = 0
    black_score = 0
    fin_jeu = end_game(board)

    pion = [0,  0,  0,  0,  0,  0,  0,  0,
50, 50, 50, 50, 50, 50, 50, 50,
10, 10, 20, 30, 30, 20, 10, 10,
 5,  5, 10, 25, 25, 10,  5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5, -5,-10,  0,  0,-10, -5,  5,
 5, 10, 10,-20,-20, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0]

    cavalier = [-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  0,  0,  0,-20,-40,
-30,  0, 10, 15, 15, 10,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 10, 15, 15, 10,  5,-30,
-40,-20,  0,  5,  5,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50]

    fou =[-20,-10,-10,-10,-10,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  5,  0,  0,  0,  0,  5,-10,
-20,-10,-10,-10,-10,-10,-10,-20]

    tour = [ 0,  0,  0,  0,  0,  0,  0,  0,
  5, 10, 10, 10, 10, 10, 10,  5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  0,  0,  0,  5,  5,  0,  0,  0]

    reine = [-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5,  5,  5,  5,  0,-10,
 -5,  0,  5,  5,  5,  5,  0, -5,
  0,  0,  5,  5,  5,  5,  0, -5,
-10,  5,  5,  5,  5,  5,  0,-10,
-10,  0,  5,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20]

    king_middlegame = [-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-20,-30,-30,-40,-40,-30,-30,-20,
-10,-20,-20,-20,-20,-20,-20,-10,
 20, 20,  0,  0,  0,  0, 20, 20,
 20, 30, 10,  0,  0, 10, 30, 20]

    king_endgame = [-50,-40,-30,-20,-20,-30,-40,-50,
-30,-20,-10,  0,  0,-10,-20,-30,
-30,-10, 20, 30, 30, 20,-10,-30,
-30,-10, 30, 40, 40, 30,-10,-30,
-30,-10, 30, 40, 40, 30,-10,-30,
-30,-10, 20, 30, 30, 20,-10,-30,
-30,-30,  0,  0,  0,  0,-30,-30,
-50,-30,-30,-30,-30,-30,-30,-50]

    for piece in board.gamecases:
        if board.gamecases[piece].couleur == "White":
            if board.gamecases[piece].tostring() != "p":
                white_score += pion[piece]
            if board.gamecases[piece].tostring() != "c":
                white_score += cavalier[piece]
            if board.gamecases[piece].tostring() != "t":
                white_score += tour[piece]
            if board.gamecases[piece].tostring() != "e":
                white_score += fou[piece]
            if board.gamecases[piece].tostring() != "r":
                white_score += reine[piece]
            if board.gamecases[piece].tostring() != "k":
                if fin_jeu:
                    white_score += king_endgame[piece]
                else:
                    white_score += king_middlegame[piece]

        if board.gamecases[piece].couleur == "Black":
            if board.gamecases[piece].tostring() != "P":
                black_score += pion[piece]
            if board.gamecases[piece].tostring() != "C":
                black_score += cavalier[piece]
            if board.gamecases[piece].tostring() != "T":
                black_score += tour[piece]
            if board.gamecases[piece].tostring() != "E":
                black_score += fou[piece]
            if board.gamecases[piece].tostring() != "R":
                black_score += reine[piece]

            if board.gamecases[piece].tostring() != "K":
                if fin_jeu:
                    black_score += king_endgame[piece]
                else:
                    black_score += king_middlegame[piece]

    return (white_score,black_score)
