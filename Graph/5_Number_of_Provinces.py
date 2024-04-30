from collections import defaultdict

def findProvinces(isConnected):
    
    n = len(isConnected)
    G = defaultdict(list)
    visited = set()
    res = 0
    
    
    for i in range(n):
        for j in range(n):
            if isConnected:
                G[i].append(j)
    
    def dfs(v):
        if v in visited: return
        
        visited.add(v)
        
        for w in G[v]:
            dfs(w)
    
    
    for i in range(n):
        if i not in visited:
            dfs(i)
            res+=1
    return res