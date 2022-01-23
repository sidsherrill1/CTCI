"""
Problem statement:
Implement a complete binary search tree.
Implement in-order, pre-order, and post-order traversals.
In-order: print left branch, then current node, then right branch for each node
Pre-order: print current node, then left branch, then right branch
Post-order: print left branch, then right branch, the current node
"""

import math

# //----------------------------------------------------------------------------------//
# //
# //


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def Trav_In_Order(root):
    if root == None:
        return

    Trav_In_Order(root.left)
    print(root.data)
    Trav_In_Order(root.right)


def Trav_Pre_Order(root):
    if root == None:
        return

    print(root.data)
    Trav_Pre_Order(root.left)
    Trav_Pre_Order(root.right)


def Trav_Post_Order(root):
    if root == None:
        return

    Trav_Post_Order(root.left)
    Trav_Post_Order(root.right)
    print(root.data)


# //***************************************************************************************//
# //
# //


def main():
    n1 = Node(10)
    n2 = Node(11)
    n3 = Node(12)
    n4 = Node(13)
    n5 = Node(14)

    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5

    print("In-order traversal:")
    Trav_In_Order(n1)

    print("Pre-order traversal:")
    Trav_Pre_Order(n1)

    print("Post-order traversal:")
    Trav_Post_Order(n1)


if __name__ == "__main__":
    main()
