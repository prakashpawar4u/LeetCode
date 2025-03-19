class MinStack:
    def __init__(self):
        # Initialize the main stack and the min stack
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        Pushes the element val onto the stack.
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # If the min stack is empty or val is less than or equal to the current minimum, push val onto the min stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        Removes the element on the top of the stack.
        :rtype: None
        """
        if self.stack:
            popped = self.stack.pop()
            # If the popped element is the current minimum, pop it from the min stack
            if popped == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        """
        Gets the top element of the stack.
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        Retrieves the minimum element in the stack.
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()