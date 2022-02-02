"""
Problem statement:
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

NOTES
Queue: first in first out
Stack: last in first out
"""
import stack

# //----------------------------------------------------------------------------------//
# //
# //

class MyQueue:

    def __init__(self):
        self.stack = stack.Stack()

    def add(self, data):
        self.stack.push(data)

    def remove(self):
        temp_stack = stack.Stack()

        node_data = self.stack.pop()
        while node_data != None:
            temp_stack.push(node_data)
            node_data = self.stack.pop()
   
        data = temp_stack.pop()
        
        node_data = temp_stack.pop()
        while node_data != None:
            self.stack.push(node_data)
            node_data = temp_stack.pop()

        return data

    def peek(self):
        return self.stack.head.data

    def is_empty(self):
        return self.stack.head == None

    def print(self):
        print("Queue:")

        temp_stack = stack.Stack()
        node_data = self.stack.pop()
        while node_data != None:
            temp_stack.push(node_data)
            node_data = self.stack.pop()

        node_data = temp_stack.pop()
        while node_data != None:
            print(node_data)
            self.stack.push(node_data)
            node_data = temp_stack.pop()


# //----------------------------------------------------------------------------------//
# //
# //


def main():
    q = MyQueue()
    q.print()

    q.add(1)
    q.print()

    q.add(2)
    q.print()

    q.add(3)
    q.print()

    q.add(4)
    q.print()

    print(f"removed: {q.remove()}")
    q.print()

    print(f"removed: {q.remove()}")
    q.print()

    q.add(99)
    q.print()
    

if __name__ == "__main__":
    main()
