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
    
    # BFS Way
    def max_dept(self,root):
        maxDept = 0
        if root is None:
            return maxDept
        
        queue = deque([root,1])
        
        while len(queue)!= 0:
            curr,dept = queue.popleft()
            maxDept = max(dept,maxDept)
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right) 
                
        return maxDept
    
    def maxDeptRecursive(self,root):
        if root is None:
            return 0
        left = self.maxDeptRecursive(root.left)
        right = self.maxDeptRecursive(root.right)
        
        return 1 + max(left,right)
    
    
    
    def bottom_left_node(self,root):
        if not root:
            
            return 0
        
        queue = deque([root])
        
        while queue:
            curr = queue.popleft()
            
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)
                
        return curr.data
    
    def maximum_level_sum(self,root):
        if not root:
            return 0
        
        max_sum = root.data
        max_level = 1
        level = 1
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            curret_sum = 0
            
            for i in range(level_size):
                curr = queue.popleft()
                curret_sum +=  curr.data
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if curret_sum > max_sum:
                max_sum = curret_sum
                max_level = level
                
            level += 1        
        return max_level
     