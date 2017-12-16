# A magic index in an array is defined to be an index such that A[i] = i.
# Given a sorted array of integers, write a method to find a magic index, if one exists,
# in array A.

# FOLLOW UP
# What if elements are not distinct?


def magic_index(seq, start, end):
    """
    Finds the magic index
    Args:
        seq: The sorted list
        start: Start index to start search from
        end: Index at which to end search
    """
    if end < start or start < 0 or end >= len(seq):
        return -1

    mid = (start + end) // 2
    if seq[mid] == mid:
        return mid
    elif seq[mid] > mid:
        return magic_index(seq, start, mid - 1)
    else:
        return magic_index(seq, mid + 1, end)

l = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
print(magic_index(l, 0, len(l)-1))
