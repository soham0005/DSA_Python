# Leetcode - 82
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next 
                prev.next = head.next
                    
            else:
                prev = prev.next
                
            head = head.next
            
        return dummy.next