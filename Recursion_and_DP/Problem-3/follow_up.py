# A magic index in an array is defined to be an index such that A[i] = i.
# Given a sorted array of integers, write a method to find a magic index, if one exists,
# in array A.

# FOLLOW UP
# What if elements are not distinct?


def magic_index_follow_up(seq, start, end):
    """
    Finds the magic index
    Args:
        seq: The sorted list
        start: Start index to start search from
        end: Index at which to end search
    """
    if end < start or start < 0 or end >= len(seq):
        return -1

    mid_index = (start + end) // 2
    mid_value = seq[mid_index]

    if mid_index == mid_value:
        return mid_index

    # Search left
    left_index = min(mid_index - 1, mid_value)
    left = magic_index_follow_up(seq, start, left_index)
    if left >= 0:
        return left

    # Search right
    right_index = max(mid_index + 1, mid_value)
    right = magic_index_follow_up(seq, right_index, end)
    return right

l = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
print(magic_index_follow_up(l, 0, len(l)-1))
