from collections import deque
import time

class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def expand(self, problem):
        return [self.child_node(problem, action) for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action)
        return next_node

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)

class NQueensProblem:
    def __init__(self, N):
        self.N = N

    def actions(self, state):
        if state[-1] != -1:
            return []
        else:
            col = state.index(-1)
            return [row for row in range(self.N) if not self.conflicted(state, row, col)]

    def result(self, state, row):
        col = state.index(-1)
        new = list(state[:])
        new[col] = row
        return tuple(new)

    def conflicted(self, state, row, col):
        return any(self.conflict(row, col, state[c], c) for c in range(col))

    def conflict(self, row1, col1, row2, col2):
        return (row1 == row2 or row1 - col1 == row2 - col2 or row1 + col1 == row2 + col2)

    def goal_test(self, state):
        return state[-1] != -1 and not any(self.conflicted(state, state[col], col) for col in range(len(state)))

    def h(self, node):
        num_conflicts = 0
        for (r1, c1) in enumerate(node.state):
            for (r2, c2) in enumerate(node.state):
                if (r1, c1) != (r2, c2):
                    num_conflicts += self.conflict(r1, c1, r2, c2)

        return num_conflicts

    def breadth_first_search(self):
        frontier = deque([Node(tuple([-1] * self.N))])

        while frontier:
            node = frontier.popleft()
            if self.goal_test(node.state):
                return node
            frontier.extend(node.expand(self))

        return None

    def depth_first_search(self):
        frontier = [Node(tuple([-1] * self.N))]

        while frontier:
            node = frontier.pop()
            if self.goal_test(node.state):
                return node
            frontier.extend(node.expand(self))

        return None

# Example usage:
n_queens_problem = NQueensProblem(9)

# Breadth-first search
start_time_bfs = time.time()
bfs_solution = n_queens_problem.breadth_first_search()
end_time_bfs = time.time()
print("Breadth-first search solution:")
print(bfs_solution.solution())
print("BFS Runtime: {:.6f} seconds".format(end_time_bfs - start_time_bfs))

# Depth-first search
start_time_dfs = time.time()
dfs_solution = n_queens_problem.depth_first_search()
end_time_dfs = time.time()
print("\nDepth-first search solution:")
print(dfs_solution.solution())
print("DFS Runtime: {:.6f} seconds".format(end_time_dfs - start_time_dfs))