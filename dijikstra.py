
import heapq
def dijkstra(graph, source):
    priority_queue = []
    heapq.heapify(priority_queue)
    distances= {node: float("inf") for node in graph}
    previous = {node: None for node in graph}
    distances[source] = 0
    heapq.heappush(priority_queue, (0, source))
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            new_distance= current_distance + weight
            
            if new_distance < distances[neighbor]:
                
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
                previous[neighbor] = current_node
    return distances, previous



graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Run Dijkstra's algorithm
start_node = 'A'

distances, previous = dijkstra(graph, start_node)

                
                
    