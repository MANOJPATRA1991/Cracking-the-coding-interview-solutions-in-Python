from Trees_and_Graphs.tree.main import BinaryTree

# Success if root.get_left_child() <= root.get_root_val() < root.get_right_child()

def check(root):
    """
    Main function to start the check for BST
    Args:
        root(BinaryTree): The root of the binary tree
    Returns:
        Boolean: Indicates whether a BST or not
    """
    return check_bst(root, None, None)


def check_bst(root, min, max):
    """
    Checks if a binary tree is a BST
    Args:
        root(BinaryTree): The root of the tree
        min(int/None)
        max(int/None)
    Returns:
        Boolean: Indicates whether a BST or not
    """
    if root is None:
        return True

    # base case
    if ((min is not None and root.get_root_val() <= min)
        or (max is not None and root.get_root_val() > max)):
        return False

    if (not check_bst(root.left_child, min, root.get_root_val())
        or not check_bst(root.right_child, root.get_root_val(), max)):
        return False

    return True


r = BinaryTree(5)
r.insert_left(3)
r.insert_right(7)
r.get_left_child().insert_left(1)
r.get_left_child().insert_right(4)

print(check(r))
