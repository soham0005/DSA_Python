class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle2(self,head):
        if head is None or head.next is None:
            return None
        
        slow = fast = head 
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            
            if slow == fast:
                slow = head
                
                while slow != fast:
                    slow = slow.next
                    fast = fast.next 
                return slow 
        return None 