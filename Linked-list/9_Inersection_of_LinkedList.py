# Gfg Intersection of Linked List.
# Return the linked list which have common values.


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Solution:
    def findIntersection(self, head1, head2):
        # code here
        # return head of intersection list
        value_set = set()
        temp = head2
        dummy = Node(None)
        curr = dummy
    
        # Store values from head2 in a set
        while temp is not None:
            value_set.add(temp.data)
            temp = temp.next
    
        temp = head1
        while temp is not None:
            if temp.data in value_set:
                curr.next = Node(temp.data)
                curr = curr.next
            temp = temp.next
    
        return dummy.next