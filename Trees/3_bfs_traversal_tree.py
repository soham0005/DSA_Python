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
    
    def Zig_Zag_BFS_Traversal(self,root):
        
        bfs = []
        flag = True
        
        if root is None:
            return bfs
        queue = deque([])
        queue.append(root)
        
        while len(queue) != 0:
            level_size = len(queue)
            curr_level = deque()
            
            for i in range(level_size):
                curr = queue.popleft()
                
                if flag:
                    curr_level.append(curr.data)
                else:
                    curr_level.appendleft(curr.data)
                
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
                    
            bfs.append(curr_level)
            flag = not flag
            
        return bfs
    
    
    def LevelOrderSuccessor(self,root,key):
        
        bfs = []        
        if root is None:
            return bfs
        queue = deque([])
        queue.append(root)
        
        while len(queue) != 0:
            curr = queue.popleft()
            
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
            
            if curr.data == key:
                break
                    
            
        return queue.popleft()




if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    
    ans = tree.LevelOrderSuccessor(tree.root,3)
    print(ans.data)