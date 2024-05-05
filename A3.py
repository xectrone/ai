import sys
from rich import print

class PGraph:
    def __init__(self, vertices, graph):
        self.V = vertices
        self.graph = graph

    def minKey(self, key, mstSet):
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        mstSet = [False] * self.V
        
        key[0] = 0
        parent[0] = -1

        for i in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        print(f'\n\nPrim’s Minimum Spanning Tree:\nEdge \tWeight')
        minimumCost = 0
        for i in range(1, self.V):
            print(f'{parent[i]} -- {i} == {self.graph[i][parent[i]]}')
            minimumCost += self.graph[i][parent[i]]
        print(f'Minimum cost = {minimumCost}')


class KGraph:
    def __init__(self, vertices, graph):
        self.V = vertices
        self.graph = []

        for i in range(self.V):
            for j in range(i, self.V):
                if graph[i][j] != 0:
                    self.graph.append([i, j, graph[i][j]])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        self.graph = sorted(self.graph, key = lambda item: item[2])
        i = 0
        e = 0
        parent = []
        rank = []
        result = []
        
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            x = self.find(parent, u)
            y = self.find(parent, v)
            i = i + 1

            if x != y:
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                e = e + 1

        minimumCost = 0
        print(f'\n\nKruskal’s Minimum Spanning Tree:\nEdge \tWeight')
        for u, v, weight in result:
            minimumCost += weight
            print(f'{u} -- {v} == {weight}')
        print(f'Minimum cost = {minimumCost}')

if __name__ == '__main__':
    graph = [
        [0, 1, 0, 0],
        [1, 0, 0, 2],
        [0, 0, 0, 3],
        [0, 2, 3, 0],
    ]

    g = PGraph(4, graph)
    g.primMST()

    g = KGraph(4, graph)
    g.KruskalMST()
