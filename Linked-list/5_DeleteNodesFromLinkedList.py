# Leetcode - 2487 

'''
Delete all Nodes from the list which are strictly greater than the current value of right side


Approach:- 
1) Revserse the Linkedlist
2) set maxEle to current node's value
3) iterate over list and delete all the nodes which are smaller than maxEle
4) If a node's value is greater than the maxEle value then keep the maxEle as current Node' value
5) Again Reverse the list and return the head

'''

class ListNode(object):
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
        
class Solution(object):
    def reverseList(self,head):
        prev = forward = None
        
        while head is not None:
            forward = head.next
            head.next = prev
            prev = head
            head = forward
            
        return prev
    
    def removeNodes(self,head):
        head = self.reverseList(head)
        current = head 
        
        maxEle = head.val
        prev = head
        head = head.next
        
        while head is not None:
            if head.val >= maxEle:
                maxEle = head.val
                prev = head
                head = head.next
            else:
                prev.next = head.next 
                head = head.next
        
        head = self.reverseList(current)
        return head
        