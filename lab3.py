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
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

def generate_goal_state(n):
    return [list(range(1, n**2+1))[i:i+n] for i in range(0, n**2, n)]

def shuffle_state(state, n, moves=100):
    state = copy.deepcopy(state)
    for _ in range(moves):
        empty_pos = [(i, j) for i in range(n) for j in range(n) if state[i][j] == n**2][0]
        possible_moves = []
        if empty_pos[0] > 0:
            possible_moves.append((-1, 0))
        if empty_pos[0] < n-1:
            possible_moves.append((1, 0))
        if empty_pos[1] > 0:
            possible_moves.append((0, -1))
        if empty_pos[1] < n-1:
            possible_moves.append((0, 1))
        move = random.choice(possible_moves)
        new_row, new_col = empty_pos[0] + move[0], empty_pos[1] + move[1]
        state[empty_pos[0]][empty_pos[1]], state[new_row][new_col] = state[new_row][new_col], state[empty_pos[0]][empty_pos[1]]
    return state

def get_successors(node, n):
    successors = []
    empty_pos = [(i, j) for i in range(n) for j in range(n) if node.state[i][j] == n**2][0]
    possible_moves = []
    if empty_pos[0] > 0:
        possible_moves.append((-1, 0))
    if empty_pos[0] < n-1:
        possible_moves.append((1, 0))
    if empty_pos[1] > 0:
        possible_moves.append((0, -1))
    if empty_pos[1] < n-1:
        possible_moves.append((0, 1))
    for move in possible_moves:
        new_row, new_col = empty_pos[0] + move[0], empty_pos[1] + move[1]
        new_state = copy.deepcopy(node.state)
        new_state[empty_pos[0]][empty_pos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_pos[0]][empty_pos[1]]
        successors.append(PuzzleNode(new_state, parent=node, action=(empty_pos[0], empty_pos[1]), depth=node.depth+1))
    return successors

def bfs(initial_state, goal_state, n):
    start_time = time.time()
    explored = set()
    frontier = deque([PuzzleNode(initial_state)])
    while frontier:
        node = frontier.popleft()
        explored.add(tuple(map(tuple, node.state)))
        if node.state == goal_state:
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
    initial_state = shuffle_state(generate_goal_state(n), n)
    goal_state = generate_goal_state(n)
    print("Anhnii tuluv:")
    for row in initial_state:
        print(row)
    print("daraagiin tuluv:")
    for row in goal_state:
        print(row)
    path, execution_time, memory_consumption = bfs(initial_state, goal_state, n)
    if path:
        print("BFS:")
        print("Uildeluud:")
        for action in path:
            print(action)
        print("Niit uildel:", len(path))
        print("Zartsuulsan hugatsaa:", execution_time)
        print("Sanah oin hereglee:", memory_consumption)
    else:
        print("BFS ashiglaj chadsangvi.")

if __name__ == "__main__":
    main()
