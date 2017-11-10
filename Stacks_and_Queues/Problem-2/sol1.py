# Problem: Design a stack with min function in addition
# to push and pop function, all of which operate O(1) time
from Stacks_and_Queues.stacks.main import Stack
import sys


class NodeWithMin(object):
    """
    A class to store values in stack along with minimum value in stack
    Attributes:
        value(Integer): The value to store
        min(Integer): The minimum value in the stack
    """
    def __init__(self, v, min):
        self.value = v
        self.min = min


class StackWithMin(Stack):
    """
    Stack to store minimum value along with items
    """
    def push(self, item):
        """
        Push an item into the stack
        Args:
            item(Integer): The item to push into the stack
        """
        new_min = min(item, self.min())
        super().push(NodeWithMin(item, new_min))

    def min(self):
        """
        Find the minimum value in the stack
        """
        if self.is_empty():
            return sys.maxsize
        return self.peek().min

x = StackWithMin()
x.push(7)
x.push(2)
x.push(5)
x.push(1)

print(x.min())