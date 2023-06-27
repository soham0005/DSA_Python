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
            
    def removeNthNode(self,N):
        slow = fast = self.head
        for i in range(N):
            fast = fast.next
        if not fast: return self.head.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next 
        slow = slow.next.next 
        return self.head
            
        
            
linkedlist = LinkedList()

linkedlist.addAtStart(40)
linkedlist.addAtStart(30)
linkedlist.addAtStart(20)
linkedlist.addAtStart(10)

# print(linkedlist.returnHead().next)
# linkedlist.displayNodes()
linkedlist.removeNthNode(2)
