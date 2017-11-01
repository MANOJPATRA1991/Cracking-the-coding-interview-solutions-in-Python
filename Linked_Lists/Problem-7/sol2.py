# Function to check if a Linked List is a Palindrome
from Linked_Lists.main.linkedList import LinkedList, Element
from Stacks_and_Queues.stacks.main import Stack


def check_palindrome(ll):
    """
    Check if a Linked List is a Palindrome
    Args:
         ll(LinkedList): The linked list to check
    Returns:
        Boolean: Indicates if linked list is a palindrome or not
    """
    fast = ll.head
    slow = ll.head

    s = Stack()

    while fast is not None and fast.next is not None:
        s.push(slow.value)
        slow = slow.next
        fast = fast.next.next

    # Handles the case of odd number of nodes in the linked list
    if fast is not None:
        slow = slow.next

    while slow is not None:
        top = s.pop()
        if top == slow.value:
            slow = slow.next
        else:
            return False
    return True

e1 = Element(0)
e2 = Element(1)
e3 = Element(2)
e4 = Element(1)
e5 = Element(0)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)

print(check_palindrome(ll))