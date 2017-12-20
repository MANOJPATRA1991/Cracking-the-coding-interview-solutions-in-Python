# You have a stack of n boxes, with widths w_{i}, heights h_{i} and
# depths d_{i}. The boxes cannot be rotated and can only be stacked on top of
# one another if each box in the stack is strictly larger than the box above
# it in width, height, and depth. Implement a method to build the tallest stack
# possible, where the height of a stack is the sum of the heights of each box.

import functools


def memoize(f):
    """ Minimalistic memoization decorator (*args / **kwargs)
    Based on: http://code.activestate.com/recipes/577219/ """

    cache = {}

    @functools.wraps(f)
    def memf(*args, **kwargs):
        fkwargs = frozenset(kwargs.items())
        if (args, fkwargs) not in cache:
            cache[args, fkwargs] = f(*args, **kwargs)
        return cache[args, fkwargs]
    return memf


@functools.total_ordering
class _Box(object):
    def __lt__(self, other):
        """
        Checks if self is less than other, i.e.,
        if self can be stacked on 'other'
        Args:
            other(Box): The box on which to stack
        """
        return (self.width < other.width and
                self.height < other.height and
                self.length < other.length)


class Box(_Box):
    """
    Creates a Box instance
    """
    def __init__(self, width, height, length):
        self.width = width
        self.length = length
        self.height = height


class Stack(frozenset):
    """
    Creates a stack of boxes
    """
    def stack_on(self, bottom):
        """
        Creates a stack that can be stacked upon bottom
        Args:
            bottom(Box): Box above which to stack
        Returns:
            Stack: Resulting stack
        """
        return Stack(box for box in self if box < bottom)

    def remove(self, current_box):
        """
        Creates a stack after removing the current box
        Args:
            current_box(Box): Box to be removed
        Returns:
            Stack: Stack created after removal of the current box
        """
        return Stack(box for box in self if box != current_box)

    @staticmethod
    def height(seq):
        """
        Find the height of a valid stack of boxes
        Args:
            seq: Stack of boxes
        Returns:
            Integer: Height of the given stack
        """
        return sum(box.height for box in seq)

    @staticmethod
    def total_height(x):
        return x[0].height + Stack.height(x[1])

    @memoize
    def find_tallest_stack(self):
        """
        Returns a sorted list of boxes that create the tallest stack
        """

        if not self:
            return []

        sub_stacks = dict()
        for box in self:
            stack_ = self.remove(box)
            stack_on_box = stack_.stack_on(box)
            sub_stacks[box] = stack_on_box.find_tallest_stack()
        bottom, stack_ = max(sub_stacks.items(), key=Stack.total_height)
        return [bottom] + stack_


b1 = Box(3, 4, 1)
b2 = Box(8, 6, 2)
b3 = Box(7, 8, 3)

stack1 = Stack([b1, b2, b3])

print(stack1.find_tallest_stack() == [b3, b1])

