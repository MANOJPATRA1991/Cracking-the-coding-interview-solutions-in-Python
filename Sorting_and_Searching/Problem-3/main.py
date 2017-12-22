# Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an
# element in the array. Assume that the array was originally sorted in increasing order.


def search(_list, left, right, x):
    """
    Search the element x
    Args:
        _list: The given list
        left: The left index
        right: The right index
        x: The value to search for
    Returns:
        Integer: Index of the element if found else -1
    """
    mid = (left + right) // 2
    # Found the element
    if x == _list[mid]:
        return mid

    # Not found
    if right < left:
        return -1

    # If left half is sorted
    if _list[left] < _list[mid]:
        # If value of x lies in between left element and mid element
        if _list[left] <= x <= _list[mid]:
            # Search the left half
            return search(_list, left, mid - 1, x)
        else:
            # Search the right half
            return search(_list, mid + 1, right, x)
    # If right half is sorted instead of left half
    elif _list[mid] < _list[left]:
        # If value of x lies in between mid element and right element
        if _list[mid] <= x <= _list[right]:
            # Search the right half
            return search(_list, mid + 1, right, x)
        else:
            # Search the left half
            return search(_list, left, mid - 1, x)
    # Left element is the same as mid element => all left half values are same
    elif _list[left] == _list[mid]:
        # If mid element is different from right element
        if _list[mid] != _list[right]:
            # Search the right half
            return search(_list, mid + 1, right, x)
        # If mid element is same as right element
        else:
            # Search the left half
            result = search(_list, left, mid - 1, x)
            # Not found
            if result == -1:
                # Search the right half
                return search(_list, mid + 1, right, x)
            # Found
            else:
                return result
    return -1

ls = [10, 15, 20, 0, 5]
print(search(ls, 0, 4, 0))

ls = [50, 5, 20, 30, 40]
print(search(ls, 0, 4, 5))
