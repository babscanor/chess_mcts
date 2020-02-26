import random
from game import *
from math import sqrt, log, inf
from evaluation import evaluate


class MCTS:
    def __init__(self,board,nb_iter ,max_depth,root ):
        self.root = root
        self.nb_iter = nb_iter
        self.max_depth = max_depth
        self.tree = {}
        self.tree[self.root] = [board, None, 0, 1, 0, []]
        self.board = board
        # 5 is for children
        # 4 score heuristic
        # 2 nb de victoires
        # 3 nb de simulations
        

    def select_node(self, leaf, C):
        print("selection")
        while len(self.tree[leaf][5]) != 0:
            #print(leaf)
            for child in self.tree[leaf][5]:
                self.tree[child][4] = (self.tree[child][2]/self.tree[child][3]) + sqrt((C*log(self.tree[child][3]))/self.tree[child][3])
            maximum = max([self.tree[child][4] for child in self.tree[leaf][5]])
            #print(self.tree[self.root][5])
            leafs = [child for child in self.tree[leaf][5] if self.tree[child][4] == maximum]
            leaf = random.choice(leafs)
        return leaf

    def expansion(self, leaf):
        print("expansion")
        enfants = children(self.tree[leaf][0], player=self.board.player_turn())
        for child in enfants :
            self.tree[leaf + str(child[1]) +"-"+ str(child[2])+"|"] = [child[0], leaf, 0, 1, 0, []]
            self.tree[leaf][5].append(leaf + str(child[1]) +"-"+ str(child[2])+"|")

    def simulate(self, leaf):
        print("simulate")
        copied_board = copy_board(self.tree[leaf][0])
        for i in range(self.max_depth):
            if copied_board.blackwin():
                return 3000
                break
            elif copied_board.whitewin():
                return 3000
                break
            player = copied_board.player_turn()
            all_move =copied_board.all_moves(player)
            picked_move = random.choice(all_move)
            move(copied_board,picked_move[0], picked_move[1])
            return  evaluate(copied_board)



    def run(self):
        for i in range (self.nb_iter):  
            print( "this is the iteration number {}".format(i) )        
            # selection
            leaf = self.select_node(self.root, 7)
            # expansion
            if not (self.board.blackwin() or self.board.whitewin()):
                self.expansion(leaf)
                leaf = self.tree[leaf][5][random.randint(0, len(self.tree[leaf][5])-1)]

                # simulation
                result = self.simulate(leaf)

            # backpropagation


            while leaf != self.root:
                self.tree[leaf][3] += 1
                self.tree[leaf][2] += result
                leaf = self.tree[leaf][1]
            self.tree[self.root][3] += 1
            self.tree[self.root][2] += result

        # renvoyer le meilleur choix possible

        for child in self.tree[self.root][5]:
            self.tree[child][4] = (self.tree[child][2]/self.tree[child][3]) + sqrt((7*log(self.tree[self.root][3]))/self.tree[child][3])
        maximum = max([self.tree[child][4] for child in self.tree[self.root][5]])
        possible_leaf = []
        for child_root in self.tree[self.root][5]:
            if self.tree[child_root][4] == maximum:
                possible_leaf.append(child_root)
        move = possible_leaf[random.randint(0,len(possible_leaf)-1)]
        print(move)
        return move
                




