def dfs(graph, start):
    stack= [start]
    visited = set()
    
    while stack:
        current =stack.pop()
        
        if current not in visited:
            visited.add(current)
            print(current)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)


graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
dfs(graph, 'A')