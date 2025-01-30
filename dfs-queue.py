from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    path=[]
    
    while queue:
        current = queue.popleft()
        path.append(current)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                
    return path

graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
	        'E': ['B', 'F'],
	        'F': ['C', 'E']
    }
print(bfs(graph, 'A'))