from main.linkedList import LinkedList, Element;


# Implement an algorithm to find the kth to last element of a singly linked list

# Recursive solutions take O(N) space due to recursive calls

# SOLUTION I -- RECURSIVE
# Here we assume k = 1 is the last element, k = 2 is the second last element and so on.
def nthToLast(head, k):
  if head is None:
    return 0
  i = nthToLast(head.next, k) + 1
  if i == k:
    print(head.value)
  return i

# SOLUTION II -- RECURSIVE
# Here we assume k = 1 is the last element, k = 2 is the second last element and so on.
# We make use of a wrapper object
class IntWrapper(object):
  def __init__(self):
    self.value = 0
  
def nthToLast2(head, k, i):
  if head is None:
    return 0
  nthToLast2(head.next, k, i)
  i.value += 1
  if i.value == k:
    print(head.value)
  return

# SOLUTION III
# Iterative Solution
# TIME COMPLEXITY = O(N)
# SPACE COMPLEXITY = O(1)
def nthToLast3(head, k):
  p1 = p2 = head
  for i in range(k-1):
    if p2 is None:
      return 0
    p2 = p2.next
  
  while p2.next is not None:
    p1 = p1.next
    p2 = p2.next
  
  return p1.value

wrapper = IntWrapper()

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

# nthToLast(ll.head, 4)
# nthToLast2(ll.head, 4, wrapper)
print(nthToLast3(ll.head, 3))
