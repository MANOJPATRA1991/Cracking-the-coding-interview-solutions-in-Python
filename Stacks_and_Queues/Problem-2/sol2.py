# Problem: Design a stack with min function in addition
# to push and pop function, all of which operate O(1) time
from Stacks_and_Queues.stacks.main import Stack
import sys


class StackWithMin(Stack):
    """
    Stack to store minimum value along with items
    Attributes:
        s2(Stack): A stack to keep track of the minimum values
    """
    def __init__(self):
        super().__init__()
        self.s2 = Stack()

    def push(self, item):
        """
        Push item into the stack
        Args:
            item(any): Item to push
        """
        if item <= self.min():
            self.s2.push(item)
        super().push(item)

    def min(self):
        """
        Find the minimum value in the stack
        """
        if self.is_empty():
            return sys.maxsize
        return self.s2.peek()

    def pop(self):
        """
        Pops an item from the stack
        Returns:
            Integer: The popped value
        """
        value = super().pop()
        if value == self.min():
            self.s2.pop()
        return value

x = StackWithMin()
x.push(7)
x.push(2)
x.push(5)
x.push(1)

print(x.pop())
print(x.min())