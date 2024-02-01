class MyQueue(object):

    def __init__(self):
        self.first = []
        self.second = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.first.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.second.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if len(self.second) == 0:
            while self.first:
                self.second.append(self.first.pop())
        return self.second[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.first) + len(self.second) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()