# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        map = {None:None}
        temp = head
        
        while temp is not None:
            map[temp] = Node(temp.val)
            temp = temp.next 
            
        temp = head
        
        while temp is not None:
            node = map[temp]
            node.next = map[temp.next]
            node.random = map[temp.random]
            temp = temp.next 
        return map[head]