class Graph:
    def __init__(self):
        self.graph= {}
        
    def bfs(self, v):
        visited=[]
        to_visit=[]
        to_visit.append(v)
        while to_visit:
            current= to_visit.pop(0)
            visited.append(current)
            
            neighbors = sorted(self.graph[current])
            
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
                    
        return visited
        
        
g = Graph()

g.graph = {
    "A" : {"B", "C"},
    "B" : {"D"},
    "C" : {"A"},
    "D" : {"E"},
    "E" : {"F"},
    "F" : {"E"}
}

print(g.bfs("A"))

