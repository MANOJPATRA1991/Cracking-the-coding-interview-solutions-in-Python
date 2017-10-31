# A function to add two numbers stored in a linked list in reverse order
# and return the result as a linked list
from Linked_Lists.main.linkedList import LinkedList, Element


class Result(object):
    def __init__(self, node=None, carry=0):
        self.node = node
        self.carry = carry
        self.ll = LinkedList()


def add_linked_lists_reversed(l1, l2):
    """
    Adds two numbers stored in a linked list in reverse order
    Args:
        l1(LinkedList)
        l2(LinkedList)
    Returns: Result as a linked list
    """
    if l1.size() < l2.size():
        l1 = add_zeroes(l1, l2.size() - l1.size())
    elif l2.size() < l1.size():
        l2 = add_zeroes(l2, l1.size() - l2.size())
    ll = LinkedList()
    carry = 0
    t1 = l1.head
    t2 = l2.head
    while t1 is not None or t2 is not None:
        sum = 0
        sum += carry
        sum += t1.value
        sum += t2.value
        carry = sum // 10
        ll.append(Element(sum % 10))
        t1 = t1.next
        t2 = t2.next
    return ll.head


def add_linked_lists(l1, l2):
    """
    Adds two numbers stored in a linked list
    Args:
        l1(LinkedList)
        l2(LinkedList)
    Returns:
        LinkedList: Result as a linked list
    """
    if l1.size() < l2.size():
        l1 = add_zeroes(l1, l2.size() - l1.size(), True)
    elif l2.size() < l1.size():
        l2 = add_zeroes(l2, l1.size() - l2.size(), True)
    ll = LinkedList()
    carry = 0
    t1 = l1.head
    t2 = l2.head
    res = add_lists_helper(t1, t2)
    return res.ll.head


def add_lists_helper(l1, l2):
    """
    Adds two numbers stored in a linked list
    Args:
        l1(Element): Head of first list
        l2(Element): Head of second list
    Returns:
        Result: Result instance
    """
    if l1 is None or l2 is None:
        result = Result()
        return result
    sum = add_lists_helper(l1.next, l2.next)
    val = int(sum.carry) + l1.value + l2.value
    result_node = Element(val % 10)
    sum.node = result_node
    sum.carry = val // 10
    sum.ll.insert(result_node, 1)
    return sum


def add_zeroes(ll, diff, front=False):
    """
    Adds zeroes to the front of the linked list
    Args:
        ll(LinkedList)
        diff(Integer): Number of zeroes to add
    Returns:
        LinkedList: The updated list
    """
    if front:
        for i in range(0, diff):
            ll.insert(Element(0), 1)
    else:
        for i in range(0, diff):
            ll.append(Element(0))
    return ll

# Addition of 167 and 53 = 220
e1 = Element(7)
e2 = Element(6)
e3 = Element(1)

r1 = Element(5)
r2 = Element(9)

l1 = LinkedList(e1)
l1.append(e2)
l1.append(e3)

l2 = LinkedList(r1)
l2.append(r2)

# rev_result = add_linked_lists_reversed(l1, l2)
#
# while rev_result is not None:
#     print(rev_result.value, '-> ', end='')
#     rev_result = rev_result.next
# print(None)

result = add_linked_lists(l1, l2)

while result is not None:
    print(result.value, '-> ', end='')
    result = result.next
print(None)
