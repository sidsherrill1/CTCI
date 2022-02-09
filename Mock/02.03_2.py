"""
Problem statement:
# implement a function to check if a binary tree is balanced. 
# for the purposes of this question, a balanced tree is defined to be a tree such that the heights
# of the two subtrees of any node never differ by more than one.
"""

# //----------------------------------------------------------------------------------//
# //
# //


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_balanced_helper(root):

    if root == None:
        return 1

    left_depth = is_balanced_helper(root.left)
    if left_depth == False:
        return False

    right_depth = is_balanced_helper(root.right)
    if right_depth == False:
        return False

    left_depth += 1
    right_depth += 1

    if abs(left_depth - right_depth) > 1:
        return False

    return max(left_depth, right_depth)


def is_balanced(root):
    if is_balanced_helper(root):
        return True
    else:
        return False


# //***************************************************************************************//
# //
# //


def main():
    six_node = Node("6")
    seven_node = Node("7")
    three_node = Node("3", six_node, seven_node)
    four_node = Node("4")
    five_node = Node("5")
    two_node = Node("2", four_node, five_node)
    one_node = Node("1", two_node, three_node)

    print(is_balanced(one_node))

    six_node = Node("6")
    three_node = Node("3", six_node)
    four_node = Node("4")
    eight_node = Node("8")
    seven_node = Node("7", eight_node)
    five_node = Node("5", seven_node)
    two_node = Node("2", four_node, five_node)
    one_node = Node("1", two_node, three_node)

    print(is_balanced(one_node))


if __name__ == "__main__":
    main()
