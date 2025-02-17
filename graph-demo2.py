class Graph:
    def __init__(self):
        self.graph ={}
        
    def insert(self, u, v):
        if u not in self.graph:
            self.graph[u] = {v}
        else:
            self.graph[u].add(v)
            
        if v not in self.graph:
            self.graph[v] = {u}
        else:
            self.graph[v].add(u)
            
    def display(self):
        for node in self.graph:
            print(f'{node}: {self.graph[node]}')
            
    
    def delete_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].discard(v)
            
        if v in self.graph and u in self.graph[v]:
            self.graph[v].discard(u)
            
    def delete_node(self, w):
        if w in self.graph:
            for neighbor in self.graph[w]:
                self.graph[neighbor].discard(w)
            
            del self.graph[w]
            
            
            
            
g= Graph()
g.insert('A', 'B')
g.insert('A', 'C')
g.delete_node('B')

g.display()