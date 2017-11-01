# Function to check if a Linked List is a Palindrome
from Linked_Lists.main.linkedList import LinkedList, Element
import copy


def check_palindrome(ll):
    """
    Check if a Linked List is a Palindrome
    Args:
         ll(LinkedList): The linked list to check
    Returns:
        Boolean: Indicates if linked list is a palindrome or not
    """
    t1 = ll
    t2 = copy.deepcopy(ll)
    LinkedList.reverse(t2)
    nxt1 = t1.head
    nxt2 = t2.head
    for i in range(0, (1 + ll.size() // 2)):
        if nxt1.value == nxt2.value:
            nxt1 = nxt1.next
            nxt2 = nxt2.next
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