"""
Problem statement:
Stack Min: How would you design a stack which, in addition to push and pop, has 
function min which returns the minimum element? Push, pop, and min should all operate
in O(1) time.
"""


# //----------------------------------------------------------------------------------//
# //
# //


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, data):
        head = Node(data)
        self.head = head
        self.min_list = [data]

    def push(self, data):
        head = Node(data, self.head)
        self.head = head
        if data <= self.min_list[0]:
            self.min_list.insert(0, data)

    def pop(self):
        old_head = self.head
        new_head = self.head.next
        self.head = new_head
        if old_head.data == self.min_list[0]:
            self.min_list.pop(0)
        return old_head.data

    def min(self):
        return self.min_list[0]

    def print(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next


# //----------------------------------------------------------------------------------//
# //
# //


def main():
    stack = Stack(1)
    print(f"min: {stack.min()}")
    stack.print()

    stack.push(2)
    print(f"min: {stack.min()}")
    stack.print()

    stack.push(-3)
    print(f"min: {stack.min()}")
    stack.print()

    stack.pop()
    print(f"min: {stack.min()}")
    stack.print()


if __name__ == "__main__":
    main()
