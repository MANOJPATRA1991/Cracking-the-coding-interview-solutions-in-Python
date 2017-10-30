# Algorithm to decide if T2 is a subtree of T1.

# A tree T2 is a subset of T1, if there exists a node n in T1 such that
# the subtree of n is identical to T2.

# Runtime complexity = O(n + km)
# n = number of nodes in T1
# m = number of nodes in T2
# k = number of times we call match_tree when T2's root matches T1's
# If the value of the nodes in T1 are in the range 0 to p,
# then, k ~= (n/p)

# Space complexity = O(log(n) + log(m))
from Trees_and_Graphs.tree.main import BinaryTree


def contains_tree(t1, t2):
    """
    Decides if T2 is a subtree of T1
    Args:
        t1(BinaryTree): The larger tree
        t2(BinaryTree): The smaller tree
    Returns:
        Boolean: Indicates if T2 is a subtree of T1 or not
    """
    # Empty tree is always a subtree
    if t2 is None:
        return True
    return sub_tree(t1, t2)


def sub_tree(r1, r2):
    """
    Helper function that decides if T2 is a subtree of T1
    Args:
        r1(BinaryTree): The larger tree
        r2(BinaryTree): The smaller tree
    Returns:
        Boolean: Indicates if T2 is a subtree of T1 or not
    """
    # If big tree is empty
    if r1 is None:
        return False
    if r1.get_root_val() == r2.get_root_val():
        if match_tree(r1, r2):
            return True
    return sub_tree(r1.left_child, r2) or sub_tree(r1.right_child, r2)


def match_tree(n1, n2):
    """
    Helper function that decides if all nodes of T2 match that of T1
    Args:
        n1(BinaryTree): The larger tree
        n2(BinaryTree): The smaller tree
    Returns:
        Boolean: Indicates if all nodes of T2 match that of T1
    """
    # If both are empty
    if n1 is None and n2 is None:
        return True
    # If one but not both are empty
    if n1 is None or n2 is None:
        return False
    # If values don't match
    if n1.get_root_val() != n2.get_root_val():
        return False
    return match_tree(n1.left_child, n2.left_child) and\
           match_tree(n1.right_child, n2.right_child)


# T1
tree1 = BinaryTree(10)
tree1.insert_left(7)
tree1.insert_right(15)
tree1.left_child.insert_left(6)
tree1.left_child.insert_right(8)
tree1.left_child.right_child.insert_right(9)
tree1.right_child.insert_left(13)
tree1.right_child.insert_right(17)

# T2
tree2 = BinaryTree(7)
tree2.insert_left(6)
tree2.insert_right(8)
tree2.right_child.insert_right(9)

print(contains_tree(tree1, tree2))