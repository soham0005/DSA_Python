# Node of a tree

class Node:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

class BinaryTree:
    diameter = 0
    
    def __init__(self):
        self.root = None
        
    
    def preOrder(self,root):
        if root is None:
            return 
        print(root.data,end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)
        
    
    def PathSum(self,root,targetSum):
        if root is None:
            return False
        
        if root.data == targetSum and root.left is None and root.right is None:
            return True

        return self.PathSum(root.left,targetSum - root.data) + self.PathSum(root.right, targetSum - root.data)
    
    
    def PathSum2(self,root,targetSum):
        ans = []
        self.helper(root,ans,[],targetSum)
        return ans
        


    def helper(self,root,ans,path,targetSum):
        if root is None:
            return
        path.append(root.data)
        
        if root.left is None and root.right is None and root.val == targetSum:
            ans.append(list(path))
        
        self.helper(root.left,ans,path,targetSum-root.data)
        self.helper(root.right,ans,path,targetSum-root.data)
        
        
    # Leetcode - 129
    def SumRootToLeafNode(self,root):
        
        def helper(root,pathSum):
            if root is None:
                return 0
            
            pathSum = pathSum * 10 + root.data
            
            if root.left is None and root.right is None:
                return pathSum
            
            return helper(root.left,pathSum) + helper(root.right,pathSum)
    
        return helper(root,0)
    
    def PathWithGivenSequence(self,root,sequence):
        def helper(root,sequence,index):
            if root is None:
                return False
            
            if root.left is None and root.right is None and root.data == sequence[index]:
                return True
            
            if index >= len(sequence) or sequence[index] != root.data:
                return False
            
            return helper(root.left,sequence,index+1) or helper(root.right,sequence,index+1)
            
        if root is None:
            return len(sequence) == 0
        
        return helper(root,sequence,0)
    
    
    def DiameterOfTree(self,root):
        
        def findHeight(root):
            if root is None:
                return 0
            
            left = findHeight(root.left)
            right = findHeight(root.right)
            
            curr = left + right
            self.diameter = max(curr,self.diameter)
            return max(left,right) + 1
        
        
        findHeight(root)
        return self.diameter
        

        
        

        
if __name__ == 'main':
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(6)
    
    
    
    
        