# Implement a queue using two stacks

from Stacks_and_Queues.stacks.main import Stack


class MyQueue(object):
    """
    Queue implementation using Stacks
    Attributes:
        stack_newest(Stack): Stack to store new incoming elements
        stack_oldest(Stack): Stack to store elements of stack_newest in reverse order
    """
    def __init__(self):
        self.stack_newest = Stack()
        self.stack_oldest = Stack()

    def size(self):
        """
        Determine the size of the stack
        Returns:
            Integer: The size of the stack
        """
        return self.stack_newest.size() + self.stack_oldest.size()

    def add(self, val):
        """
        Adds new value to queue
        Args:
            val(Integer): Value to insert in the queue
        """
        self.stack_newest.push(val)

    def shift_stacks(self):
        """
        Shift elements from stack_newest to stack_oldest
        """
        if self.stack_oldest.is_empty():
            while not self.stack_newest.is_empty():
                self.stack_oldest.push(self.stack_newest.pop())

    def peek(self):
        """
        Peeks the last element in the stack "stack_oldest"
        Returns:
            Integer: The front of the queue
        """
        self.shift_stacks()
        return self.stack_oldest.peek()

    def pop(self):
        """
        Pops the first element from the queue
        Returns:
            Integer: The popped value
        """
        self.shift_stacks()
        return self.stack_oldest.pop()

x = MyQueue()
x.add(1)
x.add(2)
x.add(3)
x.add(4)
print(x.pop())
print(x.peek())