class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        temp = dummy
        carry = 0
        
        while l1 or l2 or carry:
            sum = 0
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next 
            
            sum +=carry 
            carry = sum // 10
            node = ListNode(sum % 10)
            temp.next = node 
            temp = temp.next
            
        return dummy.next 
            
                