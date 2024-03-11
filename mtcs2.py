import random
import numpy as np
import copy

class MonteCarloTreeSearch:
    def __init__(self, exploration_weight=1, num_simulations=10000):
        self.exploration_weight = exploration_weight
        self.num_simulations = num_simulations

    def get_move(self, state):
        root = Node(state)
        pl = root.state.player()

        # Create child nodes for all available columns
        for a in state.availableCollumns():
            ss = copy.deepcopy(root)
            child_state = copy.deepcopy(ss.state)
            child_state.putGamePiece(a, pl)
            child_node = Node(child_state, parent=root)
            root.children.append(child_node)

        for _ in range(self.num_simulations):
            node = root
            while not node.state.terminal() and node.children:
                node = self.select_child(node)
            if not node.state.terminal():
                selected_child = self.expand(node)
                result = self.simulate(selected_child)
                self.backpropagate(selected_child, result)

        for c in root.children:
            print("### ",c.total_value, c.visits)
        
        best_child = max(root.children, key=lambda child: child.total_value / (child.visits + 1))
        print(best_child.total_value, best_child.visits)
        return best_child.state.last_move



    def select_child(self, node):
        #print(node.children)
        if node.parent is None:
            return node.children[0]  # Return first child if no parent
        total_visits = sum(child.visits for child in node.children)
        uct_values = [child.total_value / child.visits + self.exploration_weight * np.sqrt(np.log(total_visits) / (child.visits + 1)) for child in node.children]
        return node.children[uct_values.index(max(uct_values))]

    def simulate(self, node):
        state = copy.deepcopy(node.state)
        actions_taken = []  # Track the sequence of actions for debugging
        while not state.terminal():
            available_actions = state.availableCollumns()
            action = random.choice(available_actions)
            actions_taken.append(action)  # For debugging
            state.putGamePiece(action, state.player())

        su = state.utility()
        if self.num_simulations % 100 == 0:
            print(f"Simulations: {self.num_simulations}, Actions taken: {actions_taken}")
        if su < 0:
            return 1
        elif su == 0:
            return 0.5
        else:
            return 0

    def expand(self, node):
        unexplored_actions = [action for action in node.state.availableCollumns() if action not in [child.state.last_move for child in node.children]]
        if unexplored_actions:
            action = random.choice(unexplored_actions)
            new_state = copy.deepcopy(node.state)
            new_state.putGamePiece(action, new_state.player())
            child = Node(new_state, parent=node)
            node.children.append(child)
            return child
        else:
            if node.children:
                chosen_child = random.choice(node.children)
                return chosen_child
            else:
                return None

    def backpropagate(self, node, result):
        while node.parent:
            node.visits += 1
            node.total_value += result
            node = node.parent

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.total_value = 0  # Renamed to avoid conflict with the attribute name

    def value(self, exploration_weight):
        if self.visits == 0:
            return float('inf')
        if self.parent is not None:
            return self.total_value / self.visits + exploration_weight * np.sqrt(np.log(self.parent.visits) / (self.visits + 1))
        else:
            return self.total_value / self.visits + exploration_weight * np.sqrt(np.log(1) / (self.visits + 1))
