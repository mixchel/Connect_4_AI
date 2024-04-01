import math 
import numpy as np
import random
import copy


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
    


class MonteCarloTreeSearch:
    def __init__(self):
        self.maxIter = 10000
        self.exploring_rate = 10
        
    def get_move(self, state):
        self.peca = state.player()
        node = MCTSNode(copy.deepcopy(state))
        for _ in range(self.maxIter):
            front = self.choose(node)
            value = self.rollout(front)
            self.backprop(front, value)
        #melhor =  self.bestChild(node)
        mv = float('-inf')
        for child in node.children:
            if child.value/child.visits > mv:
                mv = child.value/child.visits
                melhor = child
            print("----", child.value, child.visits, "...", child.state.last_move, child.value/child.visits)
        print("lolada")
        return melhor.state.last_move

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



            
