import random
import numpy as np
import copy

class MonteCarloTreeSearch:
    def __init__(self, exploration_weight=10, num_simulations=1000):
        self.exploration_weight = exploration_weight
        self.num_simulations = num_simulations

    def get_move(self, state):
        root = Node(state)
        pl = root.state.player()
        print(self.num_simulations)
        bbb =0
        for _ in range(self.num_simulations):
            bbb=bbb+1
            node = root
            while not node.state.terminal() and node.children:
                node = self.select_child(node)
            if not node.state.terminal():
                selected_child = self.expand(node)
                result = self.simulate(selected_child)
                self.backpropagate(selected_child, result)
        print(bbb)
        # Print the tree structure after each simulation
        self.print_tree_structure(root)

        best_child = max(root.children, key=lambda child: child.total_value / (child.visits + 1))
        return best_child.state.last_move
    
    def print_tree_structure(self, node, indent=0):
        print(" " * indent, f"Root Node: Total Value={node.total_value}, Visits={node.visits}")
        for child in node.children:
            print(" " * (indent + 2), f"Child Node: Total Value={child.total_value}, Visits={child.visits}")




    def select_child(self, node):
        if not node.children:
            return None  # Retorna None se não houver filhos

        total_visits = sum(child.visits for child in node.children)
        uct_values = [child.total_value / (child.visits + 1) + self.exploration_weight * np.sqrt(np.log(total_visits) / (child.visits + 2)) for child in node.children]
        return node.children[np.argmax(uct_values)]

    def simulate(self, node):
        state = copy.deepcopy(node.state)
        actions_taken = []  # Track the sequence of actions for debugging
        while not state.terminal():
            available_actions = state.availableCollumns()
            action = random.choice(available_actions)
            actions_taken.append(action)  # For debugging
            state.putGamePiece(action, state.player())

        su = state.utility()
        #if self.num_simulations % 100 == 0:
        #    print(f"Simulations: {self.num_simulations}, Actions taken: {actions_taken}")
        if su < 0:
            return 1
        elif su == 0:
            return 0.5
        else:
            return 0

    def expand(self, node):
        unexplored_actions = [action for action in node.state.availableCollumns() if action not in [child.state.last_move for child in node.children]]
        new_children = []

        for action in unexplored_actions:
            new_state = copy.deepcopy(node.state)
            new_state.putGamePiece(action, new_state.player())
            child = Node(new_state, parent=node)
            new_children.append(child)
            node.children.append(child)

        if not new_children:
            total_visits = sum(child.visits for child in node.children)
            uct_values = [child.total_value / (child.visits + 1) + self.exploration_weight * np.sqrt(np.log(total_visits) / (child.visits + 2)) for child in node.children]
            return node.children[np.argmax(uct_values)] if node.children else None
        else:
            return random.choice(new_children)





    def backpropagate(self, node, result):
        while node.parent:
            node.visits += 1
            node.total_value += result
            node = node.parent

class Node:
    def __init__(self, state, parent=None):
        self.state = copy.deepcopy(state)
        self.parent = parent
        self.children = []
        self.visits = 0
        self.total_value = 0

    def value(self, exploration_weight):
        if self.visits == 0:
            return float('inf')
        if self.parent is not None:
            return self.total_value / self.visits + exploration_weight * np.sqrt(np.log(self.parent.visits) / (self.visits + 1))
        else:
            return self.total_value / self.visits + exploration_weight * np.sqrt(np.log(1) / (self.visits + 1))

