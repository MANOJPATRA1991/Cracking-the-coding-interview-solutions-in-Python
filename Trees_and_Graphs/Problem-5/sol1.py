from Trees_and_Graphs.tree.main import BinaryTree
# Implement a function to check if a binary tree is a BST
# In a BST: left <= parent < right
# This solution fails if duplicate elements are present in the binary tree
# SOLUTION 1: In-order traversal


class WrapperInt:
    """
    Helper class
    Attributes:
        index(int): To keep track of index of list to copy to
        count(int): To count the number of nodes in the tree
        val(int): Keep track of last tracked value in check_bst2()
    """
    def __init__(self):
        self.index = 0
        self.count = 0
        self.val = None

wrap = WrapperInt()


def copy_bst(root, lst):
    """
    Copies the nodes of Binary Tree into the given list
    Args:
        root(BinaryTree): The tree to copy from
        lst(List): The list to copy to
    """
    if root is None:
        return
    copy_bst(root.left_child, lst)
    lst[wrap.index] = root.get_root_val()
    wrap.index += 1
    copy_bst(root.right_child, lst)


def in_order(tree):
    """
    Counts the number of nodes in the tree
    Args:
        tree(BinaryTree)
    Returns:
         Integer: Number of nodes in the tree
    """
    if tree:
        in_order(tree.get_left_child())
        wrap.count += 1
        in_order(tree.get_right_child())
    return wrap.count


def check_bst(root):
    """
    Check if tree is a BST
    Args:
        root(BinaryTree): Root of the binary tree
    Returns:
        Boolean: Indicates if tree is a BST
    """
    count = in_order(root)
    lst = [0]*count
    copy_bst(root, lst)
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False
    return True


# SOLUTION II
def check_bst2(root):
    """
    Check if tree is a BST
    Args:
        root(BinaryTree): Root of the binary tree
    """

    if root is None:
        return True

    # Check left subtree
    if not check_bst2(root.left_child):
        return False

    # Check current node
    if wrap.val is not None and root.get_root_val() <= wrap.val:
        return False

    wrap.val = root.get_root_val()

    # Check right subtree
    if not check_bst2(root.right_child):
        return False

    return True


r = BinaryTree(5)
r.insert_left(3)
r.insert_right(7)
r.get_left_child().insert_left(1)
r.get_left_child().insert_right(4)
print(check_bst(r))
print(check_bst2(r))
