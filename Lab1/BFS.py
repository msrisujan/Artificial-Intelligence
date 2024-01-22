# Name: M.Sri Sujan
# Roll No: CS21B1081

# Breadth First Search (BFS) is an algorithm for traversing or searching tree or graph data structures.
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = set()
        queue = []
        queue.append(s)
        visited.add(s)

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)        

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("BFS traversal starting from vertex 2:")
    g.BFS(2)