# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverseList(head):
            prev = forward = None
            while head is not None:
                forward = head.next
                head.next  = prev
                prev = head
                head = forward
            return prev
        slow = fast =head

        #middle of linkedlist
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        # Reverse the Right half of the linkedlist
        slow.next = reverseList(slow.next)
        
        #point to the start of reversed list
        slow = slow.next

        while slow is not None:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True
