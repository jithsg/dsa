def dfs(graph, node, visited):
    if node not in visited:
        visited.add(node)
        print(node)
        
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

dfs(graph, 'A', set())