def bf(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    distances[start] = 0
    
    for _ in range(len(graph)-1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                new_dist = distances[node] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    predecessors[neighbor] =node
                    
    for node in graph:
        for neighbor, weight in graph[node].items():
            new_dist = distances[node] + weight
            if new_dist < distances[neighbor]:
                raise ValueError("Negative cycle deteted")
                    
    return distances, predecessors
                
graph = {
    'A': {'B': 1, 'C': 4},
	    'B': {'A': 1, 'C': 2, 'D': 5},
	    'C': {'A': 4, 'B': 2, 'D': 1},
	    'D': {'B': 5, 'C': 1}
	}

print(bf(graph, 'A'))