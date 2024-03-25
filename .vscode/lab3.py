# import numpy as np
import copy
import random
import time
from collections import deque

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

    def __eq__(self, other):
        return np.array_equal(self.state, other.state)

    def __hash__(self):
        return hash(str(self.state))

def generate_goal_state(n):
    return np.arange(1, n**2+1).reshape((n, n))

def shuffle_state(state, n, moves=100):
    for _ in range(moves): 
        empty_row, empty_col = np.where(state == n**2)
        empty_row, empty_col = empty_row[0], empty_col[0]
        possible_moves = []
        if empty_row > 0:
            possible_moves.append((-1, 0))
        if empty_row < n-1:
            possible_moves.append((1, 0))
        if empty_col > 0:
            possible_moves.append((0, -1))
        if empty_col < n-1:
            possible_moves.append((0, 1))
        move = random.choice(possible_moves)    
        new_row, new_col = empty_row + move[0], empty_col + move[1]
        state[empty_row, empty_col], state[new_row, new_col] = state[new_row, new_col], state[empty_row, empty_col]
    return state

def get_successors(node, n):
    successors = []
    empty_row, empty_col = np.where(node.state == n**2)
    empty_row, empty_col = empty_row[0], empty_col[0]
    possible_moves = []
    if empty_row > 0:
        possible_moves.append((-1, 0))
    if empty_row < n-1:
        possible_moves.append((1, 0))
    if empty_col > 0:
        possible_moves.append((0, -1))
    if empty_col < n-1:
        possible_moves.append((0, 1))
    for move in possible_moves:
        new_row, new_col = empty_row + move[0], empty_col + move[1]
        new_state = copy.deepcopy(node.state)
        new_state[empty_row, empty_col], new_state[new_row, new_col] = new_state[new_row, new_col], new_state[empty_row, empty_col]
        successors.append(PuzzleNode(new_state, parent=node, action=(empty_row, empty_col), depth=node.depth+1))
    return successors

def bfs(initial_state, goal_state, n):
    start_time = time.time()
    explored = set()
    frontier = deque([PuzzleNode(initial_state)])
    while frontier:
        node = frontier.popleft()
        explored.add(tuple(map(tuple, node.state)))
        if np.array_equal(node.state, goal_state):
            path = []
            while node.parent:
                path.append(node.action)
                node = node.parent
            path.reverse()
            execution_time = time.time() - start_time
            memory_consumption = len(explored)
            return path, execution_time, memory_consumption
        successors = get_successors(node, n)
        for successor in successors:
            if tuple(map(tuple, successor.state)) not in explored:
                frontier.append(successor)
                explored.add(tuple(map(tuple, successor.state)))
    return None, None, None

def main():
    n = 3  
    initial_state = shuffle_state(np.arange(1, n**2+1).reshape((n, n)), n)
    goal_state = generate_goal_state(n)
    print("Хольсны дараах анхны байдал:")
    print(initial_state)
    print("Зорилго:")
    print(goal_state)
    
    
    path, execution_time, memory_consumption = bfs(initial_state, goal_state, n)
    if path:
        print("BFS ашиглан:")
        print("Зорилгодоо хүрэхийн тулд хийсэн алхамууд:")
        for action in path:
            print(action)
        print("Нийт хийсэн алхам:", len(path))
        print("Зарцуулсан хугацаа:", execution_time)
        print("Санах ойн зарцуулалт(rip my ram):", memory_consumption)
    else:
        print("BFS ашиглан зорилгодоо хүрсэнгүй ээээээ.")

if __name__ == "_main_":
    main()
    