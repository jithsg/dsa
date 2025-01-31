import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
        
    def push(self, priority, value):
        heapq.heappush(self.elements, (priority, value))
        
    def pop(self):
        return heapq.heappop(self.elements)[1]
    
    def empty(self):
        return len(self.elements) == 0
    
def heuristic(node, end):
    return abs(node[0]-end[0]) + abs(node[1]-end[1])
    
def astar(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[start] = 0
    
    queue = PriorityQueue()
    queue.push(0, start)
    
    while not queue.empty():
        current = queue.pop()
        
        if current == end:
            break
    
        
        for neighbor, weight in graph[current].items():
            g_n = distances[current] + weight
            
            if g_n< distances[neighbor]:
                distances[neighbor] = g_n
                predecessors[neighbor] = current
                h_n = heuristic(neighbor, end)
                new_dist = g_n + h_n
                queue.push(new_dist, neighbor)
    
    path=[]
    curr = end
    while curr is not None:
        path.append(curr)
        curr= predecessors[curr]
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

print(astar(graph, src, dest))
            
        
    