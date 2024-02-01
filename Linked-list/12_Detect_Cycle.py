class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self,head):
        if head is None or head.next is None:
            return False
        slow = fast = head
        while(fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next 
            if fast == slow:
                return True
        return False 