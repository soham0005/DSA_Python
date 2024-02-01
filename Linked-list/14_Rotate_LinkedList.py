# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        newHead = tail = head
        if head is None or head.next is None:
            return head
        count = 1
        
        while tail.next:
            tail = tail.next 
        
        tail.next = head 
        k = k % count
        
        for i in range(count - k):
            tail = tail.next 
        newHead = tail.next
        tail.next = None
        
        return newHead