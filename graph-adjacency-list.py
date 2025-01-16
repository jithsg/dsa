class Graph:
    def __init__(self):
        self.graph={}
        
    def add(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u]= set([v])
            
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v]= set([u])
            

g= Graph()
g.add("A", "B")
g.add("A", "C")
g.add("B", "C")