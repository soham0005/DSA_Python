from collections import deque 

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

class BinaryTree:
    def __init__(self):
        self.root = None
        
    
    def preOrder(self,root):
        if root is None:
            return 
        print(root.data,end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)
        
    
    def BFS_traversal(self,root):
        bfs = []
        minimum_dept = 0
        if root is None:
            return minimum_dept
        queue = deque([])
        queue.append(root)
        
        while len(queue) != 0:
            minimum_dept += 1
            level_size = len(queue)
            
            for i in range(level_size):
                current = queue.popleft()
                
                if current.left is None and current.right is None:
                    return minimum_dept
                
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
        return minimum_dept