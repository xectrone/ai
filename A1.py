from collections import defaultdict, deque

class Graph:
    directed = True

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def DFS(self, u, v, visitSet = None) -> bool:
        visited = visitSet or set()
        visited.add(u)
        print(u,end=" ")

        if u == v:
            return True

        for neighbour in self.graph[u]:
            if neighbour not in visited:
                if self.DFS(neighbour, v, visited):
                    return True
        return False
    
    def BFS(self, u, v):
        visited = defaultdict(bool)
        queue = deque([u])
        visited[u] = True

        while queue:
            u = queue.popleft()
            print (u, end = " ")
            if u == v:
                return
            for i in self.graph[u]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if __name__ == '__main__':
    g = Graph()

    g.addEdge('A', 'B')
    g.addEdge('A', 'C')
    g.addEdge('B', 'D')
    g.addEdge('C', 'D')

    print("Following is Depth First Traversal A -> D:")
    g.DFS('A', 'D')

    print ("\n\nFollowing is Breadth First Traversal A -> D:")
    g.BFS('A', 'D')