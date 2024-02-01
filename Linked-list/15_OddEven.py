# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEven(self, head):
        if head is None or head.next is None:
            return head
        odd = head
        even =  head.next
        
        evenHead = even 
        
        while even is not None or even.next is not None:
            odd.next = odd.next.next 
            odd = odd.next 

            even.next = even.next.next 
            even = even.next 
            
        odd.next = evenHead 
        
        return head
        
        