# Sort a stack in ascending order with the help of only one additional stack

from Stacks_and_Queues.stacks.main import Stack


def sort_stack(s):
    """
    Sort a stack
    Time complexity: O(N^2)
    Space complexity: O(N)
     Args:
         s(Stack): The stack to sort
     Returns:
         Stack: Sorted stack
    """
    res = Stack()
    while not s.is_empty():
        temp = s.pop()
        while not res.is_empty() and res.peek() > temp:
            s.push(res.pop())
        res.push(temp)
    return res

x = Stack()
x.push(5)
x.push(2)
x.push(7)
x.push(3)

x = sort_stack(x)

print(x.pop())
print(x.pop())
print(x.pop())
print(x.pop())