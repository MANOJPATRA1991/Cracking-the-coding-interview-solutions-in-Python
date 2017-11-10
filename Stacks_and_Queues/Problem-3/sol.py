# Implement a SetOfStacks  of PLATES with a popAt(index) function

from stack import Stack


class SetOfStacks(object):
    """
    Class to create a list of stacks
    Attributes:
        capacity(Integer): The capacity of the SetOfStacks instance
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.__stacks = []

    def get_last_stack(self):
        """
        Get the last stack in the set of stacks
        Returns:
            Stack: The last stack in teh set of stacks
        """
        if len(self.__stacks) == 0:
            return None
        return self.__stacks[len(self.__stacks) - 1]

    def push(self, item):
        """
        Push items in set of stack
        Args:
            item(Integer): Item to push
        """
        last = self.get_last_stack()
        if last is not None and not last.is_full():
            last.push(item)
        else:
            # Create a new stack
            stack = Stack(self.capacity)
            stack.push(item)
            self.__stacks.append(stack)

    def pop(self):
        """
        Pop the last item from the last stack
        Returns:
            Integer: The value of the item popped
        """
        last = self.get_last_stack()
        value = last.pop()
        # Remove stack from set if it is empty
        if last.size() == 0:
            del self.__stacks[len(self.__stacks) - 1]
        return value

    def is_empty(self):
        """
        Checks if stack is empty
        Returns:
            Boolean: Indicates if stack is empty
        """
        last = self.get_last_stack()
        return last is None or last.is_empty()

    def pop_at(self, index):
        """
        Pop from the stack at position "index" in SetOfStacks
        Args:
            index(Integer): The position of the stack
        Returns:
            Integer: Removed item
        """
        return self.left_shift(index, True)

    def left_shift(self, index, remove_top):
        """
        Shifting of items after pop operation is performed
        Args:
            index(Integer): Position of stack in SetOfStacks
            remove_top(Boolean): Indicates if top should be removed
        Returns:
            Integer: Removed item
        """
        stack = self.__stacks[index]
        if remove_top:
            removed_item = stack.pop()
        else:
            removed_item = stack.remove_bottom()
        if stack.is_empty():
            del self.__stacks[index]
        elif len(self.__stacks) > index + 1:
                val = self.left_shift(index + 1, False)
                stack.push(val)
        return removed_item


x = SetOfStacks(3)
x.push(1)
x.push(2)
x.push(3)
x.push(4)
x.push(5)
x.push(6)
x.push(7)
x.push(8)
x.push(9)
print(x.pop_at(1))

print(x.pop_at(2))
print(x.pop_at(1))