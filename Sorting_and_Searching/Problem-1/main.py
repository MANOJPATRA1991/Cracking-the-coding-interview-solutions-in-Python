# Given two sorted lists, write a method to merge list b into list a in sorted order


def merge(list_a, list_b):
    """
    Merge two sorted lists
    Args:
        list_a: First list
        list_b: Second list
    Returns:
        List: The merged list
    """
    # last index of list A
    index_a = len(list_a) - 1

    # last index of list B
    index_b = len(list_b) - 1

    # last index of merged list
    index_merged = len(list_a) + len(list_b) - 1

    # Increase size of list A to hold the elements of
    #  list B after merging
    for i in range(len(list_b)):
        list_a.append(None)

    # Merge list A and list B starting from the last element of each
    while index_b >= 0:
        if index_a >= 0 and list_a[index_a] > list_b[index_b]:
            list_a[index_merged] = list_a[index_a]
            index_a -= 1
        else:
            list_a[index_merged] = list_b[index_b]
            index_b -= 1
        index_merged -= 1
    return list_a

listA = [1, 5, 9, 12]
listB = [2, 3, 7, 8]

result = merge(listA, listB)
print(result)
