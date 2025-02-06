class Graph:
    def __init__(self):
        self.graph = {}
        
    def add(self, u, v, weight):
        if u in self.graph.keys():
            self.graph[u].append((v, weight))
        else:
            self.graph[u] = [(v, weight)]
            
        if v in self.graph.keys():
            self.graph[v].append((u, weight))
        else:
            self.graph[v] = [(u, weight)]
            
    def display(self): 
        for key, value in self.graph.items():
            print(f"{key} : {value}")
        
g= Graph()

g.add('A', 'B', 5)
g.add('B', 'C', 10)
g.add('A', 'C', 15)
g.add('A', 'D', 20)

g.display()