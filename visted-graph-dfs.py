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
        
# def visited_disconned_graph(graph, start):
#     components = []
#     unvisited = set(graph.keys())
#     print(unvisited)
    
    # while unvisited:
    #     start = next(iter(unvisited))  # Get any unvisited node
    #     visited = dfs(graph, start)
    #     components.append(visited)
    #     unvisited -= visited
    
    # return components


    

                
graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B', 'D'],
        'D': ['C'],

    }

print(visited_disconned_graph(graph, 'A'))

        # 'E':['F', 'G'], 'F':['E'], 'G':['E']