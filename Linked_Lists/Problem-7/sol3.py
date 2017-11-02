# Function to check if a Linked List is a Palindrome
# Recursive approach
from Linked_Lists.main.linkedList import LinkedList, Element


class Result(object):
    """
    Class to store the result if match is successful
    Attributes:
        node(Element): The element to return from recursive call
        result(Boolean): Indicates if nodes from front and back at same position match
    """
    def __init__(self, node, result):
        self.node = node
        self.result = result


def check_palindrome(head, length):
    """
    Check if a Linked List is a Palindrome
    Args:
         head(Element): The head of the linked list
         length(Integer): The length of the linked list
    Returns:
        Result: A Result object
    """
    if head is None or length == 0:
        return Result(None, True)
    elif length == 1:
        return Result(head.next, True)
    elif length == 2:
        return Result(head.next.next, head.value == head.next.value)
    res = check_palindrome(head.next, length-2)
    if not res.result or res.node is None:
        return res
    else:
        res.result = (head.value == res.node.value)
        res.node = res.node.next
    return res

e1 = Element(0)
e2 = Element(1)
e3 = Element(2)
e7 = Element(3)
e8 = Element(2)
e4 = Element(1)
e5 = Element(0)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e7)
ll.append(e8)
ll.append(e4)
ll.append(e5)

p = check_palindrome(ll.head, ll.size())
print(p.result)