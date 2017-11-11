# Sort a stack in ascending order(biggest on top) with the help of merge sort

from Stacks_and_Queues.stacks.main import Stack


def merge_sort(s):
    """
    Merge sort a stack
    """
    rec_merge_sort(s, s.size())


def rec_merge_sort(st, size):
    """
    Merge sort recursively after dividing each stack
    Args:
        st(Stack): Stack to sort
        size(Integer): The size of the stack to sort
    """
    if size == 1:
        return
    else:
        size1 = size // 2
        if size % 2 == 0:
            size2 = size1
        else:
            size2 = size1 + 1
        s1 = Stack()
        s2 = Stack()
        for i in range(0, size1):
            s1.push(st.pop())
        for i in range(0, size2):
            s2.push(st.pop())
        rec_merge_sort(s1, s1.size())
        # print('s1 size is ', s1.size())
        rec_merge_sort(s2, s2.size())
        # print('s2 size is ', s2.size())
        temp = merge(s1, s2)
        for i in range(temp.size()):
            st.push(temp.pop())
        # print('st size is ', st.size())
        return


def merge(s1, s2):
    """
    Merge sub-stacks
    Args:
        s1(Stack)
        s2(Stack)
    Returns:
        Stack: Merged stack
    """
    work = Stack()
    while s1.size() > 0 and s2.size() > 0:
        if s1.peek() > s2.peek():
            work.push(s1.pop())
        else:
            work.push(s2.pop())

    while s1.size() > 0:
        work.push(s1.pop())

    while s2.size() > 0:
        work.push(s2.pop())

    return work

s = Stack()
s.push(7)
s.push(2)
s.push(5)
s.push(3)

merge_sort(s)
print("Size of sorted stack is ", s.size())

print("Element no. {0} is {1} ".format(s.size(), s.pop()))
print("Element no. {0} is {1} ".format(s.size(), s.pop()))
print("Element no. {0} is {1} ".format(s.size(), s.pop()))
print("Element no. {0} is {1} ".format(s.size(), s.pop()))

