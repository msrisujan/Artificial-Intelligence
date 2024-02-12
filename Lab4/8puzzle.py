from collections import deque

# Function to check if a given state is goal state
def is_goal_state(state):
    return state == (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Function to get possible moves from the current state
def get_possible_moves(state):
    moves = []
    zero_index = state.index(0)
    if zero_index not in [0, 1, 2]:
        moves.append('up')
    if zero_index not in [6, 7, 8]:
        moves.append('down')
    if zero_index not in [0, 3, 6]:
        moves.append('left')
    if zero_index not in [2, 5, 8]:
        moves.append('right')
    return moves

# Function to apply move to the state
def apply_move(state, move):
    zero_index = state.index(0)
    new_state = list(state)
    if move == 'up':
        new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
    elif move == 'down':
        new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
    elif move == 'left':
        new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
    elif move == 'right':
        new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
    return tuple(new_state)

# Breadth-First Search
def bfs(start_state):
    visited = set()
    queue = deque([(start_state, [])])

    while queue:
        state, path = queue.popleft()
        visited.add(state)

        if is_goal_state(state):
            return len(visited)

        for move in get_possible_moves(state):
            new_state = apply_move(state, move)
            if new_state not in visited:
                queue.append((new_state, path + [move]))

# Depth-First Search
def dfs(start_state):
    visited = set()
    stack = [(start_state, [])]

    while stack:
        state, path = stack.pop()
        visited.add(state)

        if is_goal_state(state):
            return len(path)

        for move in reversed(get_possible_moves(state)):
            new_state = apply_move(state, move)
            if new_state not in visited:
                stack.append((new_state, path + [move]))

# Test the algorithms
start_state = (1, 2, 3, 4, 5, 6, 0, 7, 8)  # Example initial state
bfs_steps = bfs(start_state)
dfs_steps = dfs(start_state)

print("BFS Steps:", bfs_steps)
print("DFS Steps:", dfs_steps)
