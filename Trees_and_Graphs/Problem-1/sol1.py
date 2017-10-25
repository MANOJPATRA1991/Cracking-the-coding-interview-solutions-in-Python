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
    return max(get_height(root.getLeftChild()), get_height(root.getRightChild())) + 1


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
    height_diff = get_height(root.getLeftChild()) - get_height(root.getRightChild())
    if abs(height_diff) > 1:
        return False
    else:
        return is_balanced(root.getLeftChild()) and is_balanced(root.getRightChild())

r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
r.insertRight('c')
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())

print(is_balanced(r))