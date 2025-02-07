def dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)
                
graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

dfs(graph, 'A', visited=set())