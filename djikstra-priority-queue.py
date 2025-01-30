import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
        
    def pop(self):
        return heapq.heappop(self.elements)[1]
    
    def push(self, priority, value):
        heapq.heappush(self.elements, (priority, value))
        
    def empty(self):
        return len(self.elements) == 0
    
def dijkstra(graph, src, dest):
    distances = {vertex: float('inf') for vertex in graph}
    predecessors = {vertex:None for vertex in graph}
    distances[src] = 0
    
    queue = PriorityQueue()
    queue.push(0, src)
    
    while not queue.empty():
        current =  queue.pop()
        
        for neighbor, weight in graph[current].items():
            new_dist = distances[current] + weight
            
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                predecessors[neighbor] = current
                queue.push(new_dist, neighbor)
    
    path = []
    curr= dest
    while curr is not None:
        path.append(curr)
        curr = predecessors[curr]
    path.reverse()
    
    return path

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A', 'D'))


	   
            