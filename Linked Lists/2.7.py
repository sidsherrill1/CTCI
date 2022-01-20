"""
Problem statement:
Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the first linked list is the exact same node (by reference) as the jth node
of the second linked list, then they are intersecting.
"""

# //----------------------------------------------------------------------------------//
# //
# //


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def Check_Repeat_Address(head, addresses):
    node = head
    while node != None:
        if id(node) in set:
            return True
        set.add(id(node))
        node = node.next
    return False


def Check_Intersection(head1, head2):
    addresses = set()
    if Check_Repeat_Address(head1, addresses) or Check_Repeat_Address(head2, addresses):


# //***************************************************************************************//
# //
# //


def main():
    print(1)


if __name__ == "__main__":
    main()
