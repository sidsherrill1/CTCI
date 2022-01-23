"""
Problem statement:
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack
exceeds some threshold. Implement a data structure that mimics this. SetOfStacks should
be composed of several stacks and should create a new stack once the previous one
exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically
to a single stack.
"""

# //----------------------------------------------------------------------------------//
# //
# //


class Node:
    def __init__(self, data, prev=None):
        self.data = data
        self.prev = prev


class SetOfStacks:
    def __init__(self, max_stack_size):
        self.max_stack_size = max_stack_size
        self.stacks = [None]
        self.current_stack = 1
        self.current_stack_size = 0

    def push(self, val):
        node = Node(val)
        # If stack is at capacity, start a new stack
        if self.current_stack_size == self.max_stack_size:
            self.stacks.append(node)
            self.current_stack += 1
            self.current_stack_size = 1

        else:
            prev_node = self.stacks[self.current_stack - 1]
            node.prev = prev_node
            self.stacks[self.current_stack - 1] = node
            self.current_stack_size += 1

    def pop(self):
        # Get head from current stack and decrement current_stack_size
        node = self.stacks[self.current_stack - 1]
        self.current_stack_size -= 1

        # If current_stack_size > 0, update head of current stack
        if self.current_stack_size > 0:
            self.stacks[self.current_stack - 1] = node.prev

        # If current_stack_size == 0, update stack, current_stack, and current_stack_size
        elif self.current_stack_size == 0:
            self.stacks.pop(current_stack)
            self.current_stack -= 1
            self.current_stack_size = self.max_stack_size

    def print_stack(self):
        for i in range(self.current_stack):
            print(f"Stack {i}")
            node = self.stacks[i]
            while node != None:
                print(node.data)
                node = node.prev


# //***************************************************************************************//
# //
# //


def main():
    l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    set_of_stacks = SetOfStacks(3)
    for c in l:
        set_of_stacks.push(c)
    set_of_stacks.print_stack()


if __name__ == "__main__":
    main()
