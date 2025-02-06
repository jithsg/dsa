class Graph:
    def __init__(self):
        self.graph = {}
        
    def add(self, u, v, weight):
        if u not in self.graph.keys():
            self.graph[u] = []
        self.graph[u].append((v, weight))
        
        if v not in self.graph.keys():
            self.graph[v] = []
        self.graph[v].append((u, weight))
        
    

g = Graph()

g.add('A', 'B', 5)
g.add('A', 'C', 15)
g.add('B', 'C', 10)
g.add('A', 'D', 20)