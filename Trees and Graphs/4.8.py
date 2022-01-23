"""
Problem statement:
First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure.
NOTE: this is not necessarily a binary search tree.
"""

# //----------------------------------------------------------------------------------//
# //
# //


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left


def Search_Down():
    return


def Move_Up():
    return


def Find_Common_Ancestor(na, nb):
    return


# //***************************************************************************************//
# //
# //


def main():
    n11 = Node(11)
    n99 = Node(99)
    n98 = Node(11)
    n1 = Node(11)
    n2 = Node(11)
    n3 = Node(11)
    n4 = Node(11)

    n11.left = n99
    n11.right = n98
    n99.right = n1
    n99.left = n2
    n98.left = n3
    n98.right = n4

    print(Find_Common_Ancestor(n99, n4))


if __name__ == "__main__":
    main()
