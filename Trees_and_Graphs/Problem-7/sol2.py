from Trees_and_Graphs.tree.main import BinaryTree
# Find the first common ancestor of two nodes in a binary tree.

# Optimized solution


class Result(object):
    """
    Class to store final result
    Attributes:
        node(BinaryTree): Represents the resulting node
        isAncestor(Boolean): Indicates if the node is the common ancestor of p and q
    """
    def __init__(self, n, is_anc):
        self.node = n
        self.isAncestor = is_anc


def common_ancestor_helper(root, p, q):
    """
    Helper function to determine the common ancestor of p and q
    Args:
        root(BinaryTree): root of the tree
        p(BinaryTree): the first node
        q(BinaryTree): the second node
    Returns:
        Result: The final result
    """
    if root is None:
        return Result(None, False)

    if root == p and root == q:
        return Result(root, True)

    rx = common_ancestor_helper(root.left_child, p, q)
    # Found common ancestor
    if rx.isAncestor:
        return rx

    ry = common_ancestor_helper(root.right_child, p, q)
    # Found common ancestor
    if ry.isAncestor:
        return ry

    if rx.node is not None and ry.node is not None:
        # Found common ancestor
        return Result(root, True)
    elif root == p or root == q:
        if rx.node is not None or ry.node is not None:
            is_ancestor = True
        else:
            is_ancestor = False
        return Result(root, is_ancestor)
    else:
        return Result(rx.node if rx.node is not None else ry.node, False)


def common_ancestor(root, p, q):
    """
    Main function to run
    Args:
        root(BinaryTree): root of the tree
        p(BinaryTree): the first node
        q(BinaryTree): the second node
    Returns:
        BinaryTree/None: A binary tree node if common ancestor exists else None
    """
    r = common_ancestor_helper(root, p, q)
    if r.isAncestor:
        return r.node
    return None


r = BinaryTree(10)
r.insert_left(7)
r.insert_right(15)
r.left_child.insert_left(6)
r.left_child.insert_right(8)
r.left_child.right_child.insert_right(9)
r.right_child.insert_left(13)
r.right_child.insert_right(17)

print(common_ancestor(r, r.left_child, r.left_child.left_child).get_root_val())