"""
Problem statement:
Write code to remove duplications from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

# //----------------------------------------------------------------------------------//
# //
# //


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):  # test
        return f"data: {self.data}"


def Delete_Node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node
    return prev_node


def Get_Head(node):
    while node.prev != None:
        node = node.prev
    return node


def Remove_Duplicates(head):
    data_set = set()
    node = head
    while True:

        if node.data in data_set:
            node = Delete_Node(node)
        else:
            data_set.add(node.data)

        if node.next == None:
            break

        node = node.next

    return Get_Head(node)


def Remove_Duplicates_No_Buffers(head):
    data_set = set()
    current = head
    while True:

        current.data
        runner = current.next
        while runner != None:
            if runner.data == current.data:
                runner = Delete_Node(runner)
            runner = runner.next

        if current.next == None:
            break

        current = current.next

    return Get_Head(current)


def Build_List(l):
    head = Node(l[0])
    prev_node = head
    for i in range(1, len(l)):
        node = Node(l[i], prev=prev_node)
        prev_node.next = node
        prev_node = node
    return Get_Head(node)  # head


def Print_LL(head):
    node = head
    while node != None:
        print(node)
        node = node.next


# //***************************************************************************************//
# //
# //


def main():
    l = ["a", "b", "c", "d", "d", "e", "f"]
    head = Build_List(l)
    print("Before removing duplicates:")
    Print_LL(head)
    head = Remove_Duplicates(head)
    print("After removing duplicates:")
    Print_LL(head)

    l = ["a", "b", "c", "d", "d", "e", "f"]
    head = Build_List(l)
    print("Before removing duplicates:")
    Print_LL(head)
    head = Remove_Duplicates_No_Buffers(head)
    print("After removing duplicates, without using buffers:")
    Print_LL(head)


if __name__ == "__main__":
    main()
