# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroups(self,head,k):
        if head is None or k == 1:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = curr = forward = dummy
        
        count = 0
        while curr.next is not None:
            count = count + 1
            curr = curr.next
        
        while count >=k:
            curr = prev.next
            forward = curr.next 
            
            for i in range(1,k):
                curr.next = forward.next 
                forward.next = prev.next 
                prev.next = forward 
                forward = curr.next 
            count = count - k
            prev = curr
        return dummy.next 
        
        