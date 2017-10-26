# Create a linked list of all the nodes at each depth of a binary tree
from Trees_and_Graphs.tree.main import BinaryTree

# N = no. of nodes in the tree
# Solution returns O(N) data => Run time = O(N)
# Number of recursive calls = Space complexity = O(log N)


def create_level_linked_list(root, lists, level):
    # base case
    if root is None:
        return

    lst = []

    # if list element with index = depth does not exist
    if len(lists) == level:
        lists.append(lst)
    # if list element with index = depth does exist
    else:
        lst = lists[level]
    lst.append(root.get_root_val())
    create_level_linked_list(root.left_child, lists, level+1)
    create_level_linked_list(root.right_child, lists, level+1)


def create_levels(root):
    lists = []
    create_level_linked_list(root, lists, 0)
    return lists

r = BinaryTree('a')
r.insert_left('b')
r.insert_right('c')
r.get_left_child().insert_left('d')
r.get_left_child().insert_right('e')
r.get_right_child().insert_left('f')
r.get_right_child().insert_right('g')

new_lists = create_levels(r)
print(new_lists)
