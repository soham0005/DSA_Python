
def dfs(graph,start,visited = None):
    
    if visited is None:
        visited = set()
    visited.add(start)
    print(start,end=" ")
    
    for ele in graph[start]:
        if ele not in visited:
            dfs(graph,ele,visited)
            
            
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS traversal starting from node 'A':")
dfs(graph, 'A')