"""
Problem statement:
Minimal tree: Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.
"""

# //----------------------------------------------------------------------------------//
# //
# //


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def Build_Tree2(l):
    return Build_Tree2_rec(l, 0, len(l) - 1)


def Build_Tree2_rec(l, start, end):
    if start >= end:
        return None

    mid = int((start + end) / 2)
    root = Node(mid)
    root.left = Build_Tree2_rec(l, start, mid - 1)
    root.right = Build_Tree2_rec(l, mid + 1, end)
    return root


# //***************************************************************************************//
# //
# //


def main():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root2 = Build_Tree2(l)
    print()


if __name__ == "__main__":
    main()
