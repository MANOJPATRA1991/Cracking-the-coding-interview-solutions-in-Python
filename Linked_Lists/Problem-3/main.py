from ..main.linkedList import LinkedList, Element
# Implement an algorithm to to delete a node in the middle of a singly linked list, given only access to that node

# TIP: This problem cannot be solved if the given node is the last node

def delete_node(n):
    if n is not None and n.next is not None:
        n.value = n.next.value
        n.next = n.next.next
    return
    
  
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
e12 = Element(12)

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
ll.append(e12)

delete_node(ll.head.next.next)
delete_node(ll.head.next.next.next)
print(ll.size())
