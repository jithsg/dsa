class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self, u, v, weight):
        if u not in self.graph.keys():
            self.graph[u] = {}
        self.graph[u][v] = weight
        
        if v not in self.graph.keys():
            self.graph[v] = {}
        self.graph[v][u] = weight

    def delete_edge(self, u, v):
        if u in self.graph.keys() and  v in self.graph[u]:
            del self.graph[u][v]
            
        if v in self.graph.keys()  and u in self.graph[v]:
            del self.graph[v][u]
    
    def delete_node(self, u):
        if u in self.graph:
            for neighbor in list(self.graph[u].keys()):
                    del self.graph[neighbor][u]
            del self.graph[u]
            
    def dfs(self):
        start = self.graph
        
        


g = Graph()

g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 15)
g.add_edge('B', 'C', 10)
g.add_edge('A', 'D', 20)