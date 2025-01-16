class Graph:
    def __init__(self, size):
        self.graph= [[False for j in range(size)] for i in range(size)]
        self.size = size
        
    def add(self, u, v):
        if u <= self.size-1 and v <= self.size-1:
            self.graph[u][v] = True
            self.graph[v][u] = True
        return False
    
    def edge_exists(self, u, v):
        if u <= self.size-1 and v <= self.size-1:
            if self.graph[u][v] == True:
                return True
            return False
        
        
    

g=Graph(5)

g.add(0,4)

g.edge_exists(0,4)
    