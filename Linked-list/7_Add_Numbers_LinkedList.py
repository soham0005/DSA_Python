# Gfg Question


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        dummy = Node(None)
        temp = dummy
        
        l1Sum = l2Sum = ""
        while first:
            l1Sum = l1Sum + str(first.data)
            first = first.next
        while second:
            l2Sum = l2Sum + str(second.data)
            second = second.next
            
        totalSum = int(l1Sum) + int(l2Sum)
        totalSum = str(totalSum)
        for i in totalSum:
            temp.next = Node(int(i))
            temp = temp.next
        return dummy.next