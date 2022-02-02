"""
Problem statement:
Implement a queue.
"""


# //----------------------------------------------------------------------------------//
# //
# //


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Queue:

    head = None
    tail = None

    def add(self, data):

        node = Node(data)

        if self.tail != None:
            self.tail.next = node
        self.tail = node

        if self.head == None:
            self.head = self.tail

    def remove(self):
        if self.head == None:
            raise Exception("Nothing to remove - Queue is empty.")

        data = self.head.data
        self.head = self.head.next

        if self.head == None:
            self.tail = self.head

        return data

    def peek(self):
        if self.head == None:
            raise Exception("Nothing to remove - Queue is empty.")

        return self.head.data

    def is_empty(self):
        return self.head == None

    def print(self):
        print("Queue:")
        node = self.head
        while node != None:
            print(node.data)
            node = node.next


# //----------------------------------------------------------------------------------//
# //
# //


def main():
    q = Queue()
    # q.remove()
    q.add(1)
    q.add(10)
    q.add(50)
    q.print()
    print(f"removed: {q.remove()}")
    q.print()
    print(f"removed: {q.remove()}")
    q.print()


if __name__ == "__main__":
    main()
