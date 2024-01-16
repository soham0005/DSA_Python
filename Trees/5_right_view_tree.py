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
        
        if root is None:
            return bfs
        queue = deque([])
        queue.append(root)
        
        while len(queue) != 0:
            level_size = len(queue)
            curr_level = []
            
            for i in range(level_size):
                curr = queue.popleft()
                curr_level.append(curr.data)
                
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
                    
            bfs.append(curr_level) 
            
        return bfs
    
    
    def right_view(self,root):
        ans = []
        if root is None:
            
            
            return ans
        
        queue = deque([])
        queue.append(root)
        
        while len(queue) != 0:
            level_size = len(queue)
            
            for i in range(level_size):
                curr = queue.popleft()
                
                if (i == level_size - 1):
                    ans.append(curr.data)
                    
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
        return ans
    
    
    def left_view(self,root):
        ans = []
        if root is None:
            return ans
        
        queue = deque([])
        queue.append(root)
        
        while len(queue) != 0:
            level_size = len(queue)
            
            for i in range(level_size):
                curr = queue.popleft()
                
                if (i == 0):
                    ans.append(curr.data)
                    
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
        return ans
    
    
    def top_view(self,root):
        from collections import deque
        if not root:
            return 
        
        queue = deque([(root,0)])
        map = {}
        
        while queue:
            curr,index = queue.popleft()
            
            if index not in map:
                map[index] = curr.data
            
            if curr.left:
                queue.append((curr.left,index-1))
            
            if curr.right:
                queue.append((curr.right,index+1))
        
        for key in sorted(map):
            print(map[key],end=" ")
            
    
    def vertical_order_traversal(self,root):
        from collections import deque,defaultdict
        if not root:
            return
        
        queue = deque([(root,0)])
        map = defaultdict(list)
        
        while queue:
            curr,index = queue.popleft()
            
            map[index].append(curr.data)
            
            if curr.left:
                queue.append((curr.left,index-1))
            if curr.right:
                queue.append((curr.right,index+1))
                
        result = [map[key] for key in sorted(map)]
        return result
            
        
        
        
        
        
        
    
if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    
    tree.top_view(tree.root)
    
    