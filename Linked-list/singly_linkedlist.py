class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



# Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    def displayNodes(self):
        temp = self.head
        
        while temp is not None:
            print(temp.data)
            temp = temp.next
            
            
    def addAtStart(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        # print("Data Added Successfully")
     
        
    def addAtLast(self,data):
        node = Node(data)
        
        if self.head == None:
            self.addAtStart(data)
        else:
            temp = self.head
            
            while temp.next!= None:
                temp = temp.next
            
            temp.next = node
            # print("Done")
        
    def addAtPosition(self,pos,data):
        node = Node(data)
        if pos == 0:
            self.addAtStart(data)
        else:
            count = 1
            temp = self.head
            while count < pos:
                temp = temp.next
                count = count + 1
            node.next = temp.next
            temp.next = node 
            print("Ok")
            
    def deleteNode(self,key):
        if self.head is None:
            return "Empty LinkedList"
        else:
            if self.head == key:
                self.head = self.head.next
            else:
                temp = self.head
                while temp is not None:
                    if temp.data == key:
                        break
                    prev = temp
                    temp = temp.next
                if temp is None:
                    return
                prev.next = temp.next
                temp = None
            
            
    
    
    
linkedlist = LinkedList()


# # linkedlist.displayNodes()
# linkedlist.addAtStart("soham")
# linkedlist.addAtStart("second")
# linkedlist.addAtLast("first")

linkedlist.addAtStart(10)
linkedlist.addAtStart(20)
linkedlist.addAtLast("Not Last Element")
linkedlist.addAtPosition(1,"Second Element")
linkedlist.deleteNode("s")
linkedlist.displayNodes()


 
# linkedlist.displayNodes()
