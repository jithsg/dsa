def dfs(graph, vertex, visited):
    if vertex not in visited:
        print(vertex)
        visited.add(vertex)
    
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
            
            

            
        
        
                
            

# Example usage
if __name__ == "__main__":
    # Example graph represented as adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("DFS starting from vertex 'A':")
    print(dfs(graph, 'A', visited=set())) # Output: A B C D E F