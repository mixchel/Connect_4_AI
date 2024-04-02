#
import math 
import numpy as np
import random
import copy
import time


class MCTSNode:

    def __init__(self, state, parent=None) -> None:
        self.visits = 1
        self.value = 0
        self.state = state
        self.parent = parent
        self.children = []
        self.children_move = []

    def full_explored(self):
        return len(self.children) == len(self.state.availableCollumns())

    def update(self, v):
        self.value = self.value + v
        self.visits +=1
    
    def add_child(self, child, move):
        self.children.append(MCTSNode(child.state, parent=self))
        self.children_move.append(move)
    


class MonteCarloTreeSearch_Mod:
    def __init__(self, maxIter=100000, exploring_rate=11):
        self.maxIter = maxIter
        self.exploring_rate = exploring_rate
        

    def get_move(self, state):
        self.peca = state.player()
        self.peca_do_outro = "X" if self.peca == "O" else "O"
        ad = state.availableCollumns()
        # Check for immediate wins for current player
        for i in ad:
            st = copy.deepcopy(state)
            st.putGamePiece(i, self.peca)
            if st.game_winner == self.peca:
                return 0, i
        
        # Check for immediate wins for opponent
        self.posicoes_vulneraveis = []
        for i in ad:
            st = copy.deepcopy(state)
            st.putGamePiece(i, self.peca_do_outro)
            if st.game_winner == self.peca_do_outro:
                self.posicoes_vulneraveis.append(i)
        time_start = time.time()
        node = MCTSNode(copy.deepcopy(state))
        for _ in range(self.maxIter):
            front = self.choose(node)
            value = self.rollout(front)
            self.backprop(front, value)
            if time.time() - time_start > 10:
                break
        #melhor =  self.bestChild(node)
    # Find the best move based on the highest average value per visit
        mv = float('-inf')
        melhor = node.children[0]
        segundo_melhor = node.children[0]
        for child in node.children:
            if child.visits > 0 and child.value / child.visits > mv:
                mv = child.value / child.visits
                segundo_melhor = melhor
                melhor = child
            elif child.visits > 0 and child.value / child.visits > segundo_melhor.value / segundo_melhor.visits:
                segundo_melhor = child
        
        # Print debug information
        for child in node.children:
            print("----", child.value, child.visits, "...", child.state.last_move, child.value/child.visits)
        #
        ## Check for low win rate but significant visits in children of the best move
        #for child in melhor.children:
        #    print("FILHO", child.state.last_move, " ----> ", child.value, child.visits, child.value/child.visits)
        #    if child.visits >= 0.1 * melhor.visits and child.value / child.visits == 0:
        #        print("Low win rate but significant visits in children of the best move.")
        #        print("Returning move corresponding to the second-best child.")
        #        return 0, segundo_melhor.state.last_move
        print(self.posicoes_vulneraveis)        
        if (melhor.state.last_move in self.posicoes_vulneraveis) and (segundo_melhor.state.last_move not in self.posicoes_vulneraveis):
            return 0, segundo_melhor.state.last_move
        return 0, melhor.state.last_move
    def choose(self, node):

        while not node.state.terminal():
            if not node.full_explored():
                return self.expand(node)
            else:
                node= self.bestChild(node)
        return node
    
    def expand(self, node):
        possible_actions = node.state.availableCollumns()
        not_used = []
        for action in possible_actions:
            if action not in node.children_move:
                not_used.append(action)
        
        ac = random.choice(not_used)
        new = copy.deepcopy(node.state)
        new.putGamePiece(ac,new.player())
        node.add_child(MCTSNode(new), ac)
        return node.children[-1]
    
    def bestChild(self, node):
        bestScore = float('-inf')
        bestChild = []
        for child in node.children:
            score = child.value/child.visits + self.exploring_rate * math.sqrt(2*math.log(node.visits)/child.visits)
            if score == bestScore:
                bestChild.append(child)
            if score> bestScore:
                bestChild = [child]
                bestScore = score
        return random.choice(bestChild)
    
    def rollout(self, node):
        new = node.state
        #print(node.state, new, new.state)
        while not new.terminal():
            new = copy.deepcopy(new)
            possible_actions = new.availableCollumns()
            if len(possible_actions) >0:
                new.putGamePiece(random.choice(possible_actions), new.player())
        
        if new.game_winner == self.peca:
            return 1
        else:
            return 0

    def backprop(self, node, value):
        while node != None:
            node.value = node.value + value
            node.visits = node.visits +1
            node = node.parent
        
        return 



            
