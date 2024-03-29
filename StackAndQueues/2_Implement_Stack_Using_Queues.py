class MyStack(object):

    def __init__(self):
        self.stack = collections.deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        deq = self.stack
        deq.append(x)
        for i in range(len(deq) - 1):
            deq.append(self.pop())
        

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


s = ["h","e","l","l","o"]
print(s[::-1])