# Remove duplicate elements from a linked list

from main.linkedList import LinkedList, Element 

def removeDuplicate(n):
  if not n.is_empty():
    curr = n.head
    dic = {curr.value: True}
    while curr.next is not None:
      if curr.next.value in dic:
        curr.next = curr.next.next
      else:
        dic[curr.next.value] = True
        curr = curr.next
        
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
removeDuplicate(ll)
print(ll.size())
