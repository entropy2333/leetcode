class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        # 辅助栈
        self.helper = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if not self.helper or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])
        

    def pop(self):
        """
        :rtype: None
        """
        if self.data:
            self.helper.pop()
            return self.data.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.helper:
            return self.helper[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()