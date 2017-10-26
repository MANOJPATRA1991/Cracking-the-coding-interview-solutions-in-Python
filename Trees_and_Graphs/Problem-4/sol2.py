from Trees_and_Graphs.tree.main import BinaryTree
import itertools


# SOLUTION II
# Run time = O(N)
def create_level_linked_list(root):
    result = []
    current = []
    if root is not None:
        current.append(root)

    while len(current) > 0:
        result.append(current)
        parents, current = current, []
        for parent in parents:
            if parent.left_child is not None:
                current.append(parent.left_child)
            if parent.right_child is not None:
                current.append(parent.right_child)

    return result

r = BinaryTree('a')
r.insert_left('b')
r.insert_right('c')
r.get_left_child().insert_left('d')
r.get_left_child().insert_right('e')
r.get_right_child().insert_left('f')
r.get_right_child().insert_right('g')


new_lists = create_level_linked_list(r)
for lst in new_lists:
    for x in lst:
        print(x.get_root_val())
    print("---------------")
