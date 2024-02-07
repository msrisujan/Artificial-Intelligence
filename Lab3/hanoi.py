from collections import deque

class State:
    def __init__(self, towers):
        self.towers = towers

    def __eq__(self, other):
        return self.towers == other.towers

    def __hash__(self):
        return hash(str(self.towers))

    def __str__(self):
        return str(self.towers)

def get_possible_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if i != j and state.towers[i] and (not state.towers[j] or state.towers[j][-1] > state.towers[i][-1]):
                new_towers = [tower[:] for tower in state.towers]
                disk = new_towers[i].pop()
                new_towers[j].append(disk)
                moves.append(State(new_towers))
    return moves

def bfs(initial_state, goal_state):
    queue = deque()
    visited = set()
    parent = {}

    queue.append(initial_state)
    visited.add(initial_state)

    while queue:
        current_state = queue.popleft()

        if current_state == goal_state:
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent.get(current_state)
            return path[::-1]

        possible_moves = get_possible_moves(current_state)
        for move in possible_moves:
            if move not in visited:
                queue.append(move)
                visited.add(move)
                print(move)
                parent[move] = current_state

    return None

def dfs(initial_state, goal_state):
    stack = [initial_state]
    visited = set()
    parent = {}

    while stack:
        current_state = stack.pop()
        if current_state in visited:
            continue
        print(current_state)

        if current_state == goal_state:
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent.get(current_state)
            return path[::-1]

        visited.add(current_state)
        possible_moves = get_possible_moves(current_state)
        for move in possible_moves:
            if move not in visited:
                stack.append(move)
                parent[move] = current_state

    return None

def dfs_limit(stack, visited, goal_state, depth_limit):
    print("Depth: ", depth_limit)
    while stack:
        current_state, depth = stack.pop()
        if current_state in visited:
            continue
        print(current_state)
        
        if current_state == goal_state:
            return current_state
        
        if depth < depth_limit:
            visited.add(current_state)
            possible_moves = get_possible_moves(current_state)
            for move in possible_moves:
                if move not in visited:
                    stack.append((move, depth + 1))
    
    return None

def ids(initial_state, goal_state):
    depth_limit = 0
    while True:
        stack = [(initial_state, 0)]
        visited = set()
        result = dfs_limit(stack, visited, goal_state, depth_limit)
        if result:
            return result
        depth_limit += 1

def tower_of_hanoi(n):
    initial_state = State([list(range(n, 0, -1)), [], []])
    goal_state = State([[], [], list(range(n, 0, -1))])
    print("BFS traversal:")
    print("")
    path = bfs(initial_state, goal_state)
    if path:
        print("Steps to solve Tower of Hanoi:")
        for i, state in enumerate(path):
            print(f"Step {i}: {state}")
    else:
        print("No solution found.")
    print("")
    print("DFS traversal:")
    print("")
    path = dfs(initial_state, goal_state)
    if path:
        print("Steps to solve Tower of Hanoi:")
        for i, state in enumerate(path):
            print(f"Step {i}: {state}")
    else:
        print("No solution found.")
    print("")
    print("IDS Traversal")
    print("")
    result = ids(initial_state, goal_state)
    if result:
        print("Solution found:")
        print(result)
    else:
        print("No solution found.")

if __name__ == "__main__":
    tower_of_hanoi(3)
