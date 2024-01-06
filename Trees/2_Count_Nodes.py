# count Nodes logic:-> if root is none return 0 else recursively call the function and add 1

# number of leaf nodes :-> if root does not have left and right return 1

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def countNodes(self,root):
        if self.root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0
    
    
    def numberOfLeafNodes(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.numberOfLeafNodes(root.left) + self.numberOfLeafNodes(root.right)
    
    def numberOfNonLeafNodes(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        return  1 + self.numberOfNonLeafNodes(root.left) + self.numberOfNonLeafNodes(root.right)
    
    
    def numberOfFullNodes(self,root):
        if root is None:
            return 0
        if root.left is None or root.right is None:
            return 0
        return  1 + self.numberOfFullNodes(root.left) + self.numberOfFullNodes(root.right)
    
    
    
if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
   
    
    
    ans = tree.countNodes(tree.root)
    leafAns = tree.numberOfFullNodes(tree.root)
    
    print(ans)
        