from collections import deque

class State:
    def __init__(self, j1, j2):
        self.j1 = j1
        self.j2 = j2

    def __eq__(self, other):
        return self.j1 == other.j1 and self.j2 == other.j2

    def __hash__(self):
        return hash((self.j1, self.j2))

    def __str__(self):
        return f"({self.j1}, {self.j2})"

def get_possible_moves(state):
    moves = []
    # Fill jug 1 from the bucket
    moves.append(State(3, state.j2))
    # Fill jug 2 from the bucket
    moves.append(State(state.j1, 5))
    # Empty jug 1
    moves.append(State(0, state.j2))
    # Empty jug 2
    moves.append(State(state.j1, 0))
    # Pour from jug 1 to jug 2
    if state.j1 > 0 and state.j2 < 5:
        transfer_amount = min(state.j1, 5 - state.j2)
        moves.append(State(state.j1 - transfer_amount, state.j2 + transfer_amount))
    # Pour from jug 2 to jug 1
    if state.j2 > 0 and state.j1 < 3:
        transfer_amount = min(state.j2, 3 - state.j1)
        moves.append(State(state.j1 + transfer_amount, state.j2 - transfer_amount))
    return moves

def bfs(initial_state, goal_state):
    queue = deque()
    visited = set()

    queue.append((initial_state, [initial_state]))
    visited.add(initial_state)

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        possible_moves = get_possible_moves(current_state)
        for move in possible_moves:
            if move not in visited:
                queue.append((move, path + [move]))
                visited.add(move)
                print(move)

    return None

def dfs(initial_state, goal_state):
    stack = [(initial_state, [initial_state])]
    visited = set()

    while stack:
        current_state, path = stack.pop()

        if current_state in visited:
            continue
        print(current_state)

        if current_state == goal_state:
            return path

        visited.add(current_state)
        possible_moves = get_possible_moves(current_state)
        for move in possible_moves:
            if move not in visited:
                stack.append((move, path + [move]))

    return None

def dfs_limit(initial_state, goal_state, depth_limit):
    stack = [(initial_state, [initial_state])]
    visited = set()
    print("Depth: ", depth_limit)

    while stack:
        current_state, path = stack.pop()
        if current_state in visited:
            continue
        print(current_state)

        if current_state == goal_state:
            return path

        if len(path) <= depth_limit:
            visited.add(current_state)
            possible_moves = get_possible_moves(current_state)
            for move in possible_moves:
                if move not in visited:
                    stack.append((move, path + [move]))

    return None


def ids(initial_state, goal_state):
    depth_limit = 0
    while True:
        result = dfs_limit(initial_state, goal_state, depth_limit)
        if result:
            return result
        depth_limit += 1

initial_state = State(0, 0)
goal_state = State(1, 0)

print("BFS traversal:")
print("")
solution = bfs(initial_state, goal_state)
if solution:
    print("Solution found using BFS:")
    for i, state in enumerate(solution):
        print(f"Step {i}: {state}")
else:
    print("No solution found using BFS.")
print("")
print("DFS traversal:")
print("")
solution = dfs(initial_state, goal_state)
if solution:
    print("Solution found using DFS:")
    for i, state in enumerate(solution):
        print(f"Step {i}: {state}")
else:
    print("No solution found using DFS.")
print("")
print("IDS traversal:")
print("")
solution = ids(initial_state, goal_state)
if solution:
    print("Solution found using IDS:")
    for i, state in enumerate(solution):
        print(f"Step {i}: {state}")
else:
    print("No solution found using IDS")