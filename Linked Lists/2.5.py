"""
Problem statement:
Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.
You are not allowed to "cheat" and just convert the linked list to an integer.
EXAMPLE
Input: (7->1->6)+(5->9->2). That is, 617+295
OUTPUT: 2->1->9. That is, 912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above process.
Input: (6->1->7)+(2->9->5). That is, 617+295
OUTPUT: 9->1->2. That is, 912.
"""

import math

# //----------------------------------------------------------------------------------//
# //
# //


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def Build_LL(l):
    num_nodes = len(l) - 1
    next_node = Node(l[num_nodes])
    for i in range(len(l) - 2, -1, -1):
        node = Node(l[i], next_node)
        next_node = node
    return node  # head


def Get_Num_Nodes(head):
    count = 1
    node = head
    while node != None:
        node = node.next
        count += 1
    return count


def Get_Total_Rev(head):
    node = head
    total = 0
    i = 0
    while node != None:
        total += node.data * math.pow(10, i)
        node = node.next
        i += 1
    return total


def Add_LL_rev(head1, head2):
    return Get_Total_Rev(head1) + Get_Total_Rev(head2)


def Get_Total(head):
    num_nodes = Get_Num_Nodes(head)
    node = head
    total = 0
    i = num_nodes - 2
    while node != None:
        total += node.data * math.pow(10, i)
        node = node.next
        i -= 1
    return total


def Add_LL(head1, head2):
    return Get_Total(head1) + Get_Total(head2)


# //***************************************************************************************//
# //
# //


def main():
    l1 = [7, 1, 6]
    l2 = [5, 9, 2]
    head1 = Build_LL(l1)
    head2 = Build_LL(l2)
    print(Add_LL_rev(head1, head2))
    l1 = [6, 1, 7]
    l2 = [2, 9, 5]
    head1 = Build_LL(l1)
    head2 = Build_LL(l2)
    print(Add_LL(head1, head2))


if __name__ == "__main__":
    main()
