import random
import numpy as np
import copy

class MonteCarloTreeSearch:
    def __init__(self, exploration_weight=100, num_simulations=1000):
        self.exploration_weight = exploration_weight
        self.num_simulations = num_simulations

    def create_child(self, node):
        if node.state.terminal():
            return

        actions = node.state.availableCollumns()
        child = {}
        pl = node.state.player()
        for action in actions:
            new_state = copy.deepcopy(node.state)
            new_state.putGamePiece(action, pl)
            child[action] = Node(new_state, parent=node)
        node.child = child


    def explore(self, node):
        # Print node for debugging (optional)
        # print(f"Root node: {node}")

        current = node

        while current.child:
            child = current.child
            max_U = max(c.getUCB(self.exploration_weight) for c in child.values())
            actions = [a for a, c in child.items() if c.getUCB(self.exploration_weight) == max_U]
            if len(actions) == 0:
                print("error")
            action = random.choice(actions)
            current = child[action]

        # Check if `current` is not None before accessing attributes
        if current is not None:
            if current.visits < 1:
                current.total_value = current.total_value + self.rollout(current)
            else:
                self.create_child(current)
                if current.child:
                    current = random.choice(list(current.child.values()))
                    # Update total_value by adding rollout value
                    current.total_value += self.rollout(current)

        current.visits += 1
        self.backpropagate(current)

    
    def backpropagate(self, node):
        parent= node
        while parent.parent :
            parent = parent.parent
            parent.visits +=1
            parent.total_value += node.total_value


            
    def rollout(self, node):
        new_game = copy.deepcopy(node.state)
        while not new_game.terminal():
            pl = new_game.player()
            action = random.choice(new_game.availableCollumns())
            new_game.putGamePiece(action, pl)

        winner = new_game.game_winner
        #print(f"Rollout Winner: {winner}")  # Added line
        if winner =="O":
            return 1
        if winner == "X":
            return 0
        else:
            return 0.5

    
    def next(self, node):
        child = node.child
        max_N = max(nd.total_value/nd.visits for nd in child.values())
        max_children = [c for a,c in child.items() if c.total_value/c.visits ==max_N]
        max_child = random.choice(max_children)
        return max_child, max_child.state.last_move

    def get_move(self, state):
        node = Node(copy.deepcopy(state))
        for i in range(self.num_simulations):
            self.explore(node)
        best_child, last_move = self.next(node)
        
        # Imprimir o total_value e as visitas para cada nó filho do nó raiz
        print("Total Value and Visits for Children of Root:")
        for action, child_node in node.child.items():
            print(f"Action: {action}, Total Value: {child_node.total_value}, Visits: {child_node.visits}, Coiso: {child_node.total_value/child_node.visits}")

        # Rastreia a ação que levou ao melhor nó filho
        for action, child_node in node.child.items():
            if child_node == best_child:
                return action


            


class Node:
    def __init__(self, state, parent=None):
        self.state = copy.deepcopy(state)
        self.parent = parent
        self.child = None
        self.visits = 0
        self.total_value = 0

    def getUCB(self, exploration_weight):
        if self.visits == 0:
            return float('inf')
        top_node =self
        if top_node.parent:
            top_node = top_node.parent
        return (self.total_value/self.visits) + exploration_weight * np.sqrt(np.log(top_node.visits)/self.visits)
