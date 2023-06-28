# Leetcode - 21
'''
Approach: Use Extra LinkedList and using loop compare the values and which is smaller assign it to the next of newly created linked and increment both the linkedlist
'''

class ListNode(object):
    def __init__(self,val,next = None):
        self.val = val
        self.next= next
        

def mergeTwoLinkedList(list1,list2):
    def mergeTwoLinkedList(self,list1,list2):
        list3 = ListNode()
        temp = list3
        
        while list1 and list2:
            if list1.val > list2.val:
                list3.next = list2
                list2 = list2.next
                list3 = list3.next 
            else:
                list3.next = list1 
                list1 = list1.next 
                list3 =list3.next
        if list1 or list2:
            list3.next = list1 if list1 else list2
        return temp.next     