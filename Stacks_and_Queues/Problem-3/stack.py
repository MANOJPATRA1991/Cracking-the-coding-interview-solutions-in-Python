class Node:
    """
    Creates a node
    Attributes:
        value(Integer): The value to create a node with
        above(Node): The node above this node
        below(Node): The node below this node
    """
    def __init__(self, value):
        self.value = value
        self.above = None
        self.below = None


class Stack:
    """
    Creates a Stack data structure
    Attributes:
        capacity(Integer): Capacity of each stack
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.__size = 0
        self.__top = None
        self.__bottom = None

    @staticmethod
    def join(above, below):
        """
        Creates a link between two nodes
        Args:
            above(Node): Points to the node above
            below(Node): Points to the node below
        """
        if below is not None:
            below.above = above
        if above is not None:
            above.below = below

    def remove_bottom(self):
        """
        Remove bottom of a stack
        Returns:
            Integer: Value of the bottom node
        """
        b = self.__bottom
        self.__bottom = self.__bottom.above
        if self.__bottom is not None:
            # Ensures there is no gap in the set of stacks
            self.__bottom.below = self.__top
            self.__top = self.__top.below
        self.__size -= 1
        return b.value

    def is_full(self):
        """
        Check if a stack is full
        Returns:
             Boolean: Indicates if stack is full
        """
        return self.capacity == self.__size

    def is_empty(self):
        """
        Checks if stack is empty
        Returns:
            Boolean: Indicates if stack is empty
        """
        return self.__size == 0

    def push(self, item):
        """
        Push item into the stack
        Args:
            item(any): Item to push
        Returns:
            Boolean: Indicates if push operation is successful
        """
        if self.__size >= self.capacity:
            return False
        self.__size += 1
        new_val = Node(item)
        if self.__size == 1:
            self.__bottom = new_val
        Stack.join(new_val, self.__top)
        self.__top = new_val
        return True

    def pop(self):
        """
        Pop item from the stack
        Returns:
            Integer: The value of the node popped from the stack
        """
        t = self.__top
        self.__top = self.__top.below
        self.__size -= 1
        return t.value

    def size(self):
        """
        Get the size of the stack
        Returns:
            Integer: Size of the stack
        """
        return self.capacity