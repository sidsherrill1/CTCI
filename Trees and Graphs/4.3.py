"""
Problem statement:
List of Depth: Given a binary tree, design an algorithm which creates a linked list of
all the nodes at each depth(e.g., if you have a tree with depth D, you'll have D linked
lists). 
"""

# //----------------------------------------------------------------------------------//
# //
# //


class Tree_Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class List_Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"{self.data}"


def List_Of_Depths_Rec(root, level, lists):
    if root == None:
        return None

    list_node = List_Node(root.data)

    if len(lists) > level:
        next_node = lists[level]
        list_node.next = next_node
        lists[level] = list_node
    elif len(lists) <= level:
        lists.append(list_node)

    List_Of_Depths_Rec(root.left, level + 1, lists)
    List_Of_Depths_Rec(root.right, level + 1, lists)

    return lists


def List_Of_Depths(root):
    lists = [None]
    return List_Of_Depths_Rec(root, 0, lists)


# //***************************************************************************************//
# //
# //


def main():
    n1 = Tree_Node(10)
    n2 = Tree_Node(11)
    n3 = Tree_Node(12)
    n4 = Tree_Node(13)
    n5 = Tree_Node(14)

    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5

    lists = List_Of_Depths(n1)
    for i, head in enumerate(lists):
        print(f"List {i}")
        node = head
        while node != None:
            print(node)
            node = node.next


if __name__ == "__main__":
    main()
