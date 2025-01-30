def bellman_ford(graph, src):
    distances = {vertex: float("inf") for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[src] = 0
    
    for _ in range(len(graph) -1):
        for vertex in graph.keys():
            for neighbor, weight in graph[vertex].items():
                new_distance = distances[vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = vertex
                    
    for vertex in graph.keys():
            for neighbor, weight in graph[vertex].items():
                new_distance = distances[vertex] + weight
                if new_distance < distances[neighbor]:
                    raise ValueError("Negative cycle detected")
                
    return distances, predecessors
graph = {
 'A': {'B': 1, 'C': 4},
'B': {'A': 1, 'C': 2, 'D': 5},
'C': {'A': 4, 'B': 2, 'D': 1},
'D': {'B': 5, 'C': 1}
	}

distances, predecessors = bellman_ford(graph, 'A')

print(distances)
print(predecessors)
