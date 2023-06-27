class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def displayNodes(self):
        temp = self.head
        
        while temp is not None:
            print(temp.data)
            temp = temp.next
            
    def returnHead(self):
        return self.head
          
    def addAtStart(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
    def reverseLinkedList(self,head):
        prev = forward = None
        
        while head is not None:
            forward  = head.next 
            head.next = prev 
            prev = head 
            head = forward
        return prev 
        
            
linkedlist = LinkedList()

linkedlist.addAtStart(10)
linkedlist.addAtStart(20)
linkedlist.addAtStart(30)
# print(linkedlist.returnHead().next)
linkedlist.displayNodes()
