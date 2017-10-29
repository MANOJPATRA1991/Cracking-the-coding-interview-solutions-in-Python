# Find the first common ancestor of two nodes in a binary tree.
# **Avoid storing additional nodes in a data structure.**
from Trees_and_Graphs.tree.main import BinaryTree

# Run time: O(N)

# Less optimal as **covers** searches all nodes under root for p and q, including the
# nodes in each subtree(root.left and root.right)


def covers(root, p):
    """
    Checks if p is a descendant of root
    Args:
         root(BinaryTree): The root of the tree
         p(BinaryTree): The node to check
    Returns:
        Boolean: Indicates whether p is in the given tree
    """
    if root is None:
        return False
    if root == p:
        return True
    return covers(root.left_child, p) or covers(root.right_child, p)


def common_ancestor_helper(root, p, q):
    if root is None:
        return None
    if root == p or root == q:
        return root
    is_p_on_left = covers(root.left_child, p)
    is_p_on_right = covers(root.left_child, q)
    # if p and q lie on opposite sides of the given root
    if is_p_on_left != is_p_on_right:
        return root

    # else, they are on the same side
    child_node = root.left_child if is_p_on_left else root.right_child

    return common_ancestor_helper(child_node, p, q)


def common_ancestor(root, p, q):
    """
    Finds common ancestor for p and q
    Args:
         root(BinaryTree): The root of the tree
         p(BinaryTree): The node to check
         p(BinaryTree): The node to check
    Returns:
        Boolean: Indicates whether p is in the given tree
    """
    if not covers(root, p) or not covers(root, q):
        return None
    return common_ancestor_helper(root, p, q)

r = BinaryTree(10)
r.insert_left(7)
r.insert_right(15)
r.left_child.insert_left(6)
r.left_child.insert_right(8)
r.left_child.right_child.insert_right(9)
r.right_child.insert_left(13)
r.right_child.insert_right(17)

print(common_ancestor(r, r.left_child.left_child, r.left_child.right_child.right_child).get_root_val())