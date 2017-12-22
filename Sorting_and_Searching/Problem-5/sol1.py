# Given an M X N matrix in which each row and each column is sorted in ascending order.
# Write a method to find an element.


def find_element(_list, elem):
    """
    Finds the element
    Args:
        _list: M X N list
        elem: Element to look for
    """
    row = 0
    col = len(_list[0]) - 1

    while row < len(_list) and col >= 0:
        # Found the element
        if _list[row][col] == elem:
            return True

        # If element is less than value at (row, col)
        # element lies to the left of column "col"
        elif _list[row][col] > elem:
            col -= 1

        # If element is greater than value at (row, col)
        # element lies below the row "row"
        else:
            row += 1

    # Not found
    return False

_ls = [[15, 20, 40, 85],
       [20, 35, 80, 95],
       [30, 55, 95, 105],
       [40, 80, 100, 120]]

print(find_element(_ls, 55))
