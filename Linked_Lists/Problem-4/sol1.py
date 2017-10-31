# Algorithm to partition a linked list around a value x,
# such that all nodes less than x com before all nodes
# greater than or equal to x

# SOLUTION 1

from Linked_Lists.main.linkedList import LinkedList, Element


def partition(node, x):
    """
    Partitions a linked list around a value x
    such that all nodes less than x com before all nodes
    greater than or equal to x
    Args:
        node(LinkedList): The head of the linked list
        x(Integer): The value around which the linked list
                    should be partitioned
    Returns:
        LinkedList: The resulting Linked List
    """
    before_start = None
    before_end = None
    after_start = None
    after_end = None


    while node is not None:
        nxt = node.next
        node.next = None
        if node.value < x:
            if before_start is None:
                before_start = node
                before_end = before_start
            else:
                before_end.next = node
                before_end = node
        else:
            if after_start is None:
                after_start = node
                after_end = after_start
            else:
                after_end.next = node
                after_end = node
        node = nxt

    if before_start is None:
        return after_start

    before_end.next = after_start
    return before_start

e1 = Element(1)
e2 = Element(7)
e3 = Element(3)
e4 = Element(5)
e5 = Element(9)
e6 = Element(2)
e7 = Element(4)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)
ll.append(e7)

result = partition(ll.head, 5)

while result is not None:
    print(result.value)
    result = result.next