import heapq

class PriorityQueue:
    
    def __init__(self):
        self.elements = []
        
    def empty(self):
        return len(self.elements) == 0
    
    def push(self, priority, value):
        heapq.heappush(self.elements, (priority, value))
        
    def pop(self):
        return heapq.heappop(self.elements)[1]
    
def heuristic(node, dest):
    return abs(node[0]- dest[0]) + abs(node[1]- dest[1])
    
def a_star_search(graph, src, dest):
    queue= PriorityQueue()
    distances = {vertex: float('inf') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[src] = 0
    queue.push(0, src)
    
    while not queue.empty():
        
        current = queue.pop()
        
        if current == dest:
            break
            
        
        for neighbor, weight in graph[current].items():
            g_n = distances[current] + weight
            
            if g_n < distances[neighbor]:
                distances[neighbor] = g_n
                predecessors[neighbor] = current
                f_n = g_n + heuristic(neighbor, dest)
                queue.push(f_n, neighbor)
                
    path = []
    pred = dest
    while pred is not None:
        path.append(pred)
        pred = predecessors.get(pred)
    path.reverse()
    return path 


graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1, (2, 2): 2},
    (2, 2): {(1, 1): 2}
}

src = (0, 0)  # Starting point
dest = (2, 2) 

print(a_star_search(graph, src, dest))
            
            
        
        
    