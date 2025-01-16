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
    
    def breadth_first_search(self, v):
        visited=[]
        to_visit=[]
        to_visit.append(v)
        
        while to_visit:
            current = to_visit.pop(0)
            visited.append(current)
            
            for neighbor in sorted(self.graph[current]):
                if neighbor not in visited and neighbor not in  to_visit:
                    to_visit.append(neighbor)
        return visited
            
            

g= Graph()

g.graph={
    "A":{"B", "C"},
    "B":{"E", "D"},
    "C":{"A"},
    "D":{"B"},
    "E":{"E"}
    }

print(g.breadth_first_search("A"))