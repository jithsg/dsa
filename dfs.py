def dfs(graph, vertex, visited=None):
    if visited is None:
        visited=set()
        
    visited.add(vertex)
    print(vertex)
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
            
            

        
graph = {
       'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
	    'E': ['B', 'F'],
	    'F': ['C', 'E']}

print(dfs(graph, 'A'))