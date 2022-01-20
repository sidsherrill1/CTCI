"""
Problem statement:
Implement an algorithm to find the kth to last element of a singly linked list.
"""

# //----------------------------------------------------------------------------------//
# //
# //


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"{self.data}"


def Count_Nodes(head):
    count = 1
    node = head
    while node.next != None:
        node = node.next
        count += 1
    return count


def Find_Kth_To_Last(head, k):
    if head == None:
        return None

    node_count = Count_Nodes(head)
    target_node = node_count - k + 1  # if k = 1, this will return the last node

    if target_node < 0:
        return None

    count = 1
    node = head
    while count < target_node:
        node = node.next
        count += 1
    return node


def Build_Linked_List(l):
    n = len(l) - 1
    next_node = Node(l[n])
    for i in range(len(l) - 2, -1, -1):
        node = Node(l[i], next=next_node)
        next_node = node
    return node  # Head


def Print_LL(head):
    node = head
    while node != None:
        print(node)
        node = node.next


# //***************************************************************************************//
# //
# //


def main():
    l = ["a", "b", "c", "d", "e", "f"]
    head = Build_Linked_List(l)
    Print_LL(head)
    print("K to last:")
    print(Find_Kth_To_Last(head, 2))


if __name__ == "__main__":
    main()
