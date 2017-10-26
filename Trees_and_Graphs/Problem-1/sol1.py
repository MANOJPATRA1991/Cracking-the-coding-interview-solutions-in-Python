from ..tree.main import BinaryTree

# A function to check if a binary tree is balanced
# Balanced tree = height of the two subtrees never differ by
# more than one


# SOLUTION 1
# RUN TIME: O(N*log(N))
def get_height(root):
    """
    Function to calculate height of tree
    Args:
        root(BinaryTree): Root of the tree
    Returns:
        Integer: Height of the tree
    """
    if root is None:
        return 0
    return max(get_height(root.get_left_child()), get_height(root.get_right_child())) + 1


def is_balanced(root):
    """
    Check if a binary tree is balanced
    Args:
         root(BinaryTree): The root of the binary tree
    Returns:
        Boolean: Indicates whether the tree is balanced or not
    """
    if root is None:
        return True
    height_diff = get_height(root.get_left_child()) - get_height(root.get_right_child())
    if abs(height_diff) > 1:
        return False
    else:
        return is_balanced(root.get_left_child()) and is_balanced(root.get_right_child())

r = BinaryTree('a')
print(r.get_root_val())
print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right('c')
r.insert_right('c')
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val('hello')
print(r.get_right_child().get_root_val())

print(is_balanced(r))