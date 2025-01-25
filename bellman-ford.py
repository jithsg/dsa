def bellman_ford(graph, start):
    distances = {node: float("inf") for node in graph}
    predecessors = {node:None for node in graph}
    distances[start]=0
    
    for _ in range(len(graph)-1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                new_distance = distances[node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = node
    
    for node in graph:
            for neighbor, weight in graph[node].items():
                new_distance = distances[node] + weight
                if new_distance < distances[neighbor]:
                    raise ValueError("Negative weights detected")
                
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