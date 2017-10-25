# Remove duplicate elements from a linked list

from Linked_Lists.main.linkedList import LinkedList, Element


# SOLUTION I
# TIME COMPLEXITY = O(N)
def remove_duplicate(n):
    """
    Remove duplicate elements from a linked list
    Args:
        n: Linked List instance
    """
    if not n.is_empty():
        curr = n.head
        dic = {curr.value: True}
        while curr.next is not None:
            if curr.next.value in dic:
                curr.next = curr.next.next
            else:
                dic[curr.next.value] = True
                curr = curr.next


# SOLUTION II
#TIME COMPLEXITY = O(N^2)
# def removeDuplicate(linkedlist):
#       currNode = linkedlist.head
#       while currNode != None:
#           runner = currNode
#           while runner.next != None:
#               if runner.next.value == currNode.value:
#                   runner.next = runner.next.next
#               else:
#                   runner = runner.next
#           currNode = currNode.next

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(1)
e6 = Element(2)
e7 = Element(3)
e8 = Element(4)
e9 = Element(1)
e10 = Element(2)
e11 = Element(3)
e12 = Element(4)

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

print(ll.size())
remove_duplicate(ll)
print(ll.size())
