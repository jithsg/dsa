from collections import deque
def bfs(graph, start):
    queue = deque()
    visited= set()
    queue.append(start)
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
    
    print("BFS starting from vertex 'A':")
    print(bfs(graph, 'A'))