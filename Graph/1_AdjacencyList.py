
class AdjacencyList:

    # Adjacency Matrix
    def build_graph(self,edges,n):
    
        graph = []
  
        for i in range(n):
            graph.append(list())
            
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        return graph

    #  Adjacency List
    def build_graph_list(self,grid,n):
        
        for i in range(n):
            print(i,end=" : ")
            
            for j in range(n):
                if grid[i][j] == 1:
                    print(j,end=" ")
            print()
            
    # Adjacency String List
    def buid_graph_string_list(self,edges):
        graph  = dict()
        
        for edge in edges:
            source = edge[0]
            dest = edge[1]

            if source not in graph:
                graph[source] = list()
            graph[source].append(dest)
            
            if dest not in graph:
                graph[dest] = list()
            graph[dest].append(source)

        return graph
        
    

if __name__ == '__main__':
    
    edges = [[0,1],[0,2],[1,2],[1,3],[1,4],[2,5],[3,4],[3,5]]
    n = 6
    
    adjacencyList = AdjacencyList()
    
    # graph = adjacencyList.build_graph(edges,n)
    # print(graph)
    
    # for i in range(n):
    #     print(i,end=" : ")
        
    #     for nbr in graph[i]:
    #         print(nbr,end=" ")
    #     print()
    
    grid = [
        [0,1,1,0],
        [1,1,0,0],
        [0,1,0,1],
        [0,1,1,0]
    ]
    n = 4
    
    # adjMatrix = adjacencyList.build_graph_list(grid,n)
    
    edges = [
        ["DEL","PNQ"],
        ["DEL","SUR"],
        ["KNP","CST"],
        ["KNP","PNQ"],
        ["SUR","KNP"],
        ["DEL","KNP"],
    ]
    
    result = listString = adjacencyList.buid_graph_string_list(edges)
    print(result)