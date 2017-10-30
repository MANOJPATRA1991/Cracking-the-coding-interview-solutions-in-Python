# Algorithm to print all paths which sum to a given value

# Run time complexity = O(n*log(n))
# Space complexity = O(log n)
from Trees_and_Graphs.tree.main import BinaryTree
import sys


def depth(node):
    """
    Helper function to find the depth of a tree
    Args:
        node(BinaryTree): The tree whose depth to calculate
    Returns:
        Integer: Depth of the tree
    """
    if node is None:
        return 0
    else:
        return 1 + max(depth(node.left_child), depth(node.right_child))


def print_path(path, start, end):
    """
    Prints the node values in the path
    Args:
        path(List): A List to store the values of the nodes
        start(Integer): Start printing from here
        end(Integer): Stop printing here
    """
    for i in range(start, end+1):
        print(path[i])
    print("\n")


def find_sum(node, _sum, path, level):
    """
    Helper function to find all paths which sum up to the given value
    Args:
        node(BinaryTree): The node to start calculating
        _sum(Integer): The given sum
        path(List): The List instance to store the values
        level(Integer): The level in which the node is located
    """
    if node is None:
        return

    # Insert current node into path
    path[level] = node.get_root_val()

    # Find paths with given sum that end with this node
    temp = 0
    for i in range(level, -1, -1):
        temp += path[i]
        if temp == _sum:
            print_path(path, i, level)

    find_sum(node.left_child, _sum, path, level+1)
    find_sum(node.right_child, _sum, path, level+1)

    path[level] = -sys.maxsize - 1


def main(node, _sum):
    """
    Main function to call
    Args:
        node(BinaryTree): The node to begin calculating
        _sum(Integer): The given sum
    """
    d = depth(node)
    path = [0]*d
    find_sum(node, _sum, path, 0)

tree1 = BinaryTree(10)
tree1.insert_left(7)
tree1.insert_right(15)
tree1.left_child.insert_left(6)
tree1.left_child.insert_right(8)
tree1.left_child.right_child.insert_right(9)
tree1.right_child.insert_left(13)
tree1.right_child.insert_right(17)

main(tree1, 24)
