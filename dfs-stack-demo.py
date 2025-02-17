from collections import deque
def dfs(graph, start):
    queue = deque()
    queue.append(start)
    visited = []
    
    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.append(current)
            print(current)
            
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
            

graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
dfs(graph, 'A')