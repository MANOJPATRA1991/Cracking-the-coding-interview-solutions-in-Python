# In a BST, left <= current < right
# Find the next node(in-order successsor) of a given node in a BST
from Trees_and_Graphs.tree.main import BinaryTree


class BST(BinaryTree):
    def __init__(self, root):
        super().__init__(root)

    @staticmethod
    def left_most_child(root):
        """
        Find the left-most child of a subtree
        Args:
            root(BinaryTree): Root of the tree
        Returns:
            BinaryTree: The left most node of the tree
        """
        if root is None:
            return None
        while root.left_child is not None:
            root = root.left_child
        return root

    def in_order_succ(self, n):
        """
        Find the next in order successor of the given node
        Args:
            n(BinaryTree): The given node
        Returns:
            BinaryTree: The next node
        """
        if n is None:
            return None

        if n.right_child is not None:
            return self.left_most_child(n.right_child)
        else:
            q = n
            x = n.get_parent()
            while x is not None and x.left_child is not q:
                q = x
                x = q.get_parent()
            return x


r = BST(10)
r.insert_left(7)
r.insert_right(15)
r.left_child.insert_left(6)
r.left_child.insert_right(8)
r.left_child.right_child.insert_right(9)
r.right_child.insert_left(13)
r.right_child.insert_right(17)
print(r.in_order_succ(r.right_child.left_child).get_root_val())


