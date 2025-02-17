def dfs(graph, start):
    stack = [start]
    visited= set()
    
    while stack:
        
        current = stack.pop()
        
        if current not in visited:
            visited.add(current)
    
            
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
    return visited


def are_all_nodes_visited(graph, start):
    visited = dfs(graph, start)
    if len(graph) == len(visited):
        print("All nodes are visited, graph is connected")
    else:
        print("All nodes are not visited")

                
graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A'],
        'D': ['B'],
        'E': [],
        'F': []
    }

are_all_nodes_visited(graph, 'A')