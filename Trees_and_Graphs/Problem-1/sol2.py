from Trees_and_Graphs.tree.main import BinaryTree

# A function to check if a binary tree is balanced
# Balanced tree = height of the two subtrees never differ by
# more than one


# SOLUTION II
# RUN TIME: O(N)
# SPACE COMPLEXITY: O(N)
def check_height(root):
    """
    Check height difference
    Args:
        root(BinaryTree)
    Returns:
        Integer: 0 if root is None,
                -1 if height difference of subtrees is greater than 1
                height of the tree if difference in height of subtrees
                is less than 1
    """
    if root is None:
        return 0

    # Check if left subtree is balanced
    left_height = check_height(root.get_left_child())
    if left_height == -1:
        return -1

    # Check if right child is unbalanced
    right_height = check_height(root.get_right_child())
    if right_height == -1:
        return -1

    height_diff = left_height - right_height
    if abs(height_diff) > 1:
        return -1
    else:
        return max(left_height, right_height) + 1


def is_balanced(root):
    """
    Check if tree is balanced
    root(BinaryTree): The root of the tree
    Returns:
         Boolean: Indicates if tree is balanced
    """
    if check_height(root) == -1:
        return False
    else:
        return True


r = BinaryTree('a')
print(r.get_root_val())
print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val('hello')
print(r.get_right_child().get_root_val())

print(is_balanced(r))