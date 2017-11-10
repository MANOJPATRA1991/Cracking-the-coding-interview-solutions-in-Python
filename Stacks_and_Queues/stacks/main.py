class Stack:
    """
    Creates a Stack data structure
    Attributes:
        items(List): A list instance to store stack items,
        capacity(Integer): Capacity of each stack
    """
    def __init__(self, capacity=0):
        if capacity == 0:
            self.items = []
        else:
            self.items = [0] * capacity
        self.capacity = capacity

    def is_full(self):
        """
        Checks if stack is full
        Returns:
            Boolean: Indicates if stack is full
        """
        return not self.is_empty() and len(self.items) == self.capacity

    def is_empty(self):
        """
        Checks if stack is empty
        Returns:
            Boolean: Indicates if stack is empty
        """
        return self.items == []

    def push(self, item):
        """
        Push item into the stack
        Args:
            item(any): Item to push
        """
        if not self.is_full():
            self.items.append(item)

    def pop(self):
        """
        Pop item from the stack
        """
        if self.size() > 0:
            return self.items.pop()

    def peek(self):
        """
        Peek last item in the stack
        """
        return self.items[len(self.items) - 1]

    def size(self):
        """
        Get the size of the stack
        Returns:
            Integer: Size of the stack
        """
        return len(self.items)

