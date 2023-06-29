# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        tempA = headA
        tempB = headB
        
        while tempA!=tempB:
            tempA = headB if tempA is None else tempA.next 
            tempB = headA if tempB is None else tempB.next 
            
        return tempB
            