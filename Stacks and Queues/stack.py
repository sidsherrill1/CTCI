"""
Problem statement:
Implement a stack.
"""


# //----------------------------------------------------------------------------------//
# //
# //

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.visited = False


class Stack:

    head = None

    def push(self, data):
        node = Node(data, self.head)
        self.head = node

    def pop(self):
        if self.head == None:
            return None

        old_head = self.head
        new_head = old_head.next
        self.head = new_head
        return old_head.data

    def peek(self):
        if self.head == None:
            return None
        return self.head.data

    def isEmpty(self):
        return self.head == None

    def print(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next


# //----------------------------------------------------------------------------------//
# //
# //


def main():
    s = Stack()
    # q.remove()
    s.push(1)
    s.push(10)
    s.push(50)
    s.print()
    print(f"removed: {s.pop()}")
    s.print()
    print(f"removed: {s.pop()}")
    s.print()


if __name__ == "__main__":
    main()
