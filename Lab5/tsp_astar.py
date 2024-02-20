INF = float("inf")

graph = [[0, 12, 10, 19, 8],
         [12, 0, 3, 7, 6],
         [10, 3, 0, 2, 20],
         [19, 7, 2, 0, 4],
         [8, 6, 20, 4, 0]]
         
def enqueue(queue, tpl):
    path, g_n, f_n = tpl
    for i in range(len(queue)):
        if f_n >= queue[i][-1]:
            queue.insert(i, tpl)
            break
    else:
        queue.append(tpl)

def a_star_tsp(graph, start):
    n = len(graph)
    queue = [([start], 0, 0)]
    min_cost = INF
    min_path = []
    
    while queue:
        path, cost, h_cost = queue.pop()
        current = path[-1]
        for neighbour in range(n):
            if graph[current][neighbour] and neighbour not in path:
                if len(path + [neighbour]) == n:
                    cost += graph[current][neighbour] + graph[neighbour][start]
                    min_cost = cost
                    min_path = path + [neighbour, start]
                    return min_path, min_cost
                
                g_n = cost + graph[current][neighbour]
                h_n = remaining_mst(graph, path + [neighbour])
                f_n = g_n + h_n
                enqueue(queue, (path + [neighbour], g_n, f_n))
        
    return min_path, min_cost

def remaining_graph(graph, path):
    n = len(graph)
    new_graph = [[0 if i in path[1:-1] or j in path[1:-1] else graph[i][j] for i in range(n)] for j in range(n)]
    return new_graph

def remaining_mst(graph, path):
    n = len(graph)
    m = n - len(path[1:-1])
    graph = remaining_graph(graph, path)
    selected = [False for i in range(n)]
    selected[path[0]] = True
    mst_cost = 0
    edges = 0
    while edges < m - 1:
        min_cost = INF
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j]:
                        if min_cost > graph[i][j]:
                            min_cost = graph[i][j]
                            x = i
                            y = j
        selected[y] = True
        mst_cost += min_cost
        edges += 1
    return mst_cost

start = 0
path, cost = a_star_tsp(graph, start)
print("Path:", path)
print("Cost:", cost)
    