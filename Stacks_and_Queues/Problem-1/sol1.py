# Approach 1: Fixed Division


class Error(Exception):
    """Base class for other exceptions"""
    pass


class EmptyStackException(Error):
    """Raised when stack is empty"""
    pass


class FullStackException(Error):
    """Raised when stack is full"""
    pass


class ArrayStack:
    """
    Creates a Stack data structure
    Attributes:
        items(List): A list instance to store stack items
        stack_pointer(List): A list of pointers to keep track of stack index
        num_of_stacks(Integer): Number of stacks
        stack_size(Integer): Size of each stack
    """
    def __init__(self, num_of_stacks=3, stack_size=3):
        self.items = [0]*stack_size*num_of_stacks
        self.stack_size= stack_size
        self.stack_pointer = [-1]*num_of_stacks

    def is_empty(self, stack_num):
        """
        Checks if a stack is empty
        Args:
            stack_num(Integer): The stack number to check
                    0 corresponds to 1, 1 to 2 and so on.
        Returns:
            Boolean: Indicates if stack is empty
        """
        return self.stack_pointer[stack_num] == -1

    def push(self, stack_num, item):
        """
        Push item into the stack
        Args:
            stack_num(Integer): The stack number to check
                    0 corresponds to 1, 1 to 2 and so on.
            item(Any): Item to push
        """
        try:
            if self.stack_pointer[stack_num] + 1 >= self.stack_size:
                raise FullStackException
        except FullStackException:
            print("Stack {0} is full!!".format(stack_num))
        self.stack_pointer[stack_num] += 1
        self.items[self.stack_top(stack_num)] = item

    def pop(self, stack_num):
        """
        Pop item from the stack
        Args:
            stack_num(Integer): The stack number to check
                    0 corresponds to 1, 1 to 2 and so on.
        """
        try:
            if self.is_empty(stack_num):
                raise EmptyStackException
        except EmptyStackException:
            print("Cannot peek as Stack {0} is empty!!".format(stack_num))
        top = self.items[self.stack_top(stack_num)]
        self.items[self.stack_top(stack_num)] = 0
        self.stack_pointer[stack_num] -= 1
        return top

    def peek(self, stack_num):
        """
        Peeks last item in the stack
        Args:
            stack_num(Integer): The stack number to check
                    0 corresponds to 1, 1 to 2 and so on.
        """
        try:
            if self.is_empty(stack_num):
                raise EmptyStackException
        except EmptyStackException:
            print("Cannot peek as Stack {0} is empty!!".format(stack_num))
        index = self.stack_top(stack_num)
        return self.items[index]

    def size(self):
        """
        Get the size of the stack
        Returns:
            Integer: Size of the stack
        """
        return len(self.items)

    def stack_top(self, stack_num):
        """
        Find index of top of stack "stack_num" in absolute terms
        Args:
            stack_num(Integer): The stack number to check
                    0 corresponds to 1, 1 to 2 and so on.
        Returns:
            Integer: Top of stack "stack_num"
        """
        return stack_num * self.stack_size + self.stack_pointer[stack_num]

x = ArrayStack()
x.push(0, 0)
x.push(0, 1)
x.push(0, 2)
x.push(1, 3)
x.push(1, 4)
x.push(1, 5)
x.push(2, 6)
x.push(2, 7)
x.push(2, 8)
# should throw exception
x.push(2, 9)