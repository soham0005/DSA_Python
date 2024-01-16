# Node of a tree

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
        
    def inOrder(self,root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data)
        self.inOrder(root.right)
    
    
    def postOrder(self,root):
        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data)
        
    
    def BalancedTree(self,root):
        
        def check(root):
            if root is None:
                return 0
            
            left = check(root.left)
            right = check(root.right)
            
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            
            return max(left,right) + 1
        return check(root) != -1
        
if __name__ == 'main':
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(6)
    
    
    
    
        