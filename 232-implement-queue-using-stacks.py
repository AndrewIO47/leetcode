from inspect import stack


class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

        # if not self.stack1:
        #     self.stack1.append(x)
        # else:
        #     for i in self.stack1:
        #         self.stack2.append(i)

        #     self.stack1.append(x)
        #     for i in self.stack2:
        #         self.stack1.append(i)

    def pop(self):
        """
        :rtype: int
        """
        for i in self.stack1:
            self.stack2.append(i)

        self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        for i in self.stack1:
            self.stack2.append(i)
        self.stack2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
