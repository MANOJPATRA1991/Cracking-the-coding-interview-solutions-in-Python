# Create a BST with minimal height
# Given: A sorted array with unique integer elements
from Trees_and_Graphs.tree.main import BinaryTree


def create_bst(lst, start, end):
    """
    Create a BST with minimal height
    Args:
        lst(List): A sorted array with unique integer elements
        start(int): Starting index
        end(int): Last index
    Returns:
        Integer/None: Value of root of each subtree
    """
    if end < start:
        return None
    mid = (start + end) // 2
    root = BinaryTree(lst[mid])
    root.left_child = create_bst(lst, start, mid - 1)
    root.right_child = create_bst(lst, mid + 1, end)
    # post-order traversal
    print(root.get_root_val())
    return root


sorted_lst = [1, 2, 3, 4, 5, 6, 7, 8]
cnt = len(sorted_lst)
create_bst(sorted_lst, 0, cnt - 1)
