from collections import defaultdict, deque

class Graph:
    
    def __init__(self):
        
        self.graph = defaultdict(list)
        
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
        
        
        
        
    def bfs(self,start):
        visited = set() 
        queue = deque([start])
        
        while queue:
            
            curr = queue.popleft()
            
            if curr not in visited:
                print(curr,end=" ")
                visited.add(curr)
                
                for ele in self.graph[curr]:
                    if ele not in visited:
                        queue.append(ele)
                        
    
    
    
    
       