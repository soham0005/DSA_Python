class Node:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

class BinaryTree:
    from collections import deque
    def __init__(self):
        self.root = None
        
    
    def preOrder(self,root):
        if root is None:
            return 
        print(root.data,end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)
        
    # Lowest Common Ancestor
    
    def LCA(self,root,p,q):
        
        if root is None:
            return None
        
        if root.data == p.data or root.data == q.data:
            return root

        left = self.LCA(root.left,p,q)
        right = self.LCA(root.right,p,q)
        
        if left is not None and right is not None:
            return root
        
        return left if left is not None else right
    
    
    # def BurningTree(self,root,target):
    #     from collections import deque
    #     queue = deque([])
    #     if root is None:
    #         return 0
        
    #     if root.data == target:
    #         print(root.data)
            
    #         if root.left is not None:
    #             queue.append(root.left)
    #         if root.right is not None:
    #             queue.append(root.right)
    #         return 1
        
    #     # left call
    #     left = self.BurningTree(root.left,target)
        
    #     if(left == 1):
    #         size = len(queue)
            
    #         for i in range(size):
    
    def RootToNodePath(self,root,target):
        def getPath(root,target,ans):
            if not root:
                return False
            ans.append(root.data)
            
            if root.data == target:
                return True

            if getPath(root.left,target,ans) or getPath(root.right,target,ans):
                return True

            ans.pop()
            return False

        ans = []
        if root is None:
            return ans
        getPath(root,target,ans)
        return ans
    
    
    def AllRootToLeafNodePath(self,root):
        def getPath(root,ans = [], path = []):
            if not root:
                return ans
            path.append(root.data)
            
            if root.left is None and root.right is None:
                ans.append(list(path))
            
            getPath(root.left,ans,path)
            getPath(root.right,ans,path)
            path.pop()
            return ans

        ans = getPath(root,[],[])
        return ans
            
    # Indexing of trees then calculate the the difference which is maximum
    def maximumWidthOfTree(self,root):
        from collections import deque
        
        if not root:
            return 0
        res = 0
        queue = deque([root,1,0])
        
        prevLevel = 0
        prevNum = 1 
        while queue:
            curr,num,level = queue.popleft()
            
            if level > prevLevel:
                prevLevel = level
                prevNum = num
            res = max(res,num - prevNum + 1)
            
            
            if curr.left:
                queue.append([curr.left,2 * num,level+1])
            if curr.right:
                queue.append([curr.right,2 * num + 1,level+1])
            
        return res
    
    def AllNodeDistanceK(self,root,target,k):
        from collections import deque
        map = {}
        q = deque([root])
        
        while q:
            curr = q.popleft()
            if curr.left:
                map[curr.left] = curr
                q.append(curr.left)
            if curr.right:
                map[curr.right] = curr
                q.append(curr.right)
        
        visited = set()
        q = deque([target])
        count = 0
        
        while count != k:
            for i in range(len(q)):
                curr = q.popleft()
                
                if curr.left and curr.left not in visited:
                    q.append(curr.left)
                    visited.add(curr.left)
                
                if curr.right and curr.right not in visited:
                    q.append(curr.right)
                    visited.add(curr.right)
                
                if curr in map and map[curr] not in visited:
                    q.append(map[curr])
                    visited.add(map[curr])
            count += 1
        ans = []
        while q:
            ans.append(q.pop().data)
        return ans
                    
                
            
        
               
        


if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(6)
    
    ans = tree.AllRootToLeafNodePath(tree.root)
    print(ans)
    
    