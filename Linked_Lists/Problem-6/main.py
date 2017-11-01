# An algorithm which returns the node at the beginning of the loop

# STEPS INVOLVED:
# 1. Create two pointers: SlowPointer and StartPointer
# 2. Move FastPointer at a rate of 2 steps and SlowPointer at a rate of 1 step
# 3. When they collide, move SlowPointer to LinkedList head. Keep FastPointer where it is.
# 4. Move SlowPointer and FastPointer at a rate of one step. Return the new collision point.

from Linked_Lists.main.linkedList import LinkedList, Element


def find_beginning(head):
    # Step 1
    slow = head
    fast = head

    # Step 2
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # Check for no loop existence
    if fast is None or fast.next is None:
        return None

    # Step 3
    slow = head

    # Step 4
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast.value

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)
e6 = Element(6)
e7 = Element(7)
e8 = Element(8)
e9 = Element(9)
e10 = Element(10)
e11 = Element(11)
e11.next = e4

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)
ll.append(e6)
ll.append(e7)
ll.append(e8)
ll.append(e9)
ll.append(e10)
ll.append(e11)

print(find_beginning(ll.head))