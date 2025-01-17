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
    
    def bfs_search(self, start, end):
        visited =[]
        to_visit= []
        to_visit.append(start)
        path={start: None}
        
        while to_visit:
            current = to_visit.pop(0)
            visited.append(current)
            
            neighbors = sorted(self.graph[current])
            
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
                    path[neighbor]= current
                    
        path_list=[]
        current = end
            
        while current is not None:
            path_list.append(current)
            current = path[current]
        path_list.reverse()
        return path_list
                
            
        
        
        
g = Graph()
g.graph = {
       "A":{"B", "C"},
      "B" : {"D"},
       "C" : {"A"},
       "D" : {"B", "E"},
       "E":{"F"},
       "F":{"E"}
      }

# Let's run BFS starting from vertex 'A'
result = g.bfs_search('A', 'F')
print(result)

