# Given a sorted array of strings which is interspersed with empty strings,
# write a method to find the location of a given string


def search(_list, _str, first, last):
    """
    Search the element
    Args:
        _list: A list of strings
        _str: The string to be searched
        first: The first index
        last: The last index
    """
    # Invalid state
    if _str is None or _str == '' or _list is None:
        return -1

    # Invalid state
    if first > last:
        return -1

    # Find the mid value
    mid = (first + last) // 2

    # If mid value is empty, find the closest non-empty string
    while not _list[mid]:
        left = mid - 1
        right = mid + 1

        # Invalid state
        if left < first and right > last:
            return -1

        # Valid closest non-empty string on the left
        elif left >= first and _list[left]:
            mid = left
            break

        # Valid closest non-empty string on the right
        elif right <= last and _list[right]:
            mid = right
            break

        # If closest non-empty string still not found
        right += 1
        left += 1

    # Once closest non-empty string is found, compare it to the given string
    if _str == _list[mid]:
        return mid
    elif _str > _list[mid]:
        return search(_list, _str, mid + 1, last)
    else:
        return search(_list, _str, first, mid - 1)

ls = ['abc', '', '', 'cde', '', 'ghi', '', 'kl']
print(search(ls, 'ce', 0, len(ls)-1))           # -1
print(search(ls, 'ghi', 0, len(ls)-1))          # 5
