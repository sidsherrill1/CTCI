"""
Problem statement:
Describe how you could use a single array to implement three stacks.

PLAN:
array = size n
stack 1: [0,n/3)
stack 2: [n/3,2*n/3)
stack 3: [2*n/3,n)

stack methods are pop, push, peek, and is_empty

"""

import math

# //----------------------------------------------------------------------------------//
# //
# //


class MultiStack:

    num_of_stacks = 3

    def __init__(self, stack_space):
        self.stack_space = stack_space
        self.array_size = stack_space * self.num_of_stacks
        self.array = [None] * self.array_size
        self.stack_size = [0] * self.num_of_stacks

    def Find_Start(self, stack_num):
        stack_num_index = stack_num - 1
        return (stack_num_index) * self.stack_space

    def Find_Top_Index(self, stack_num):
        start = self.Find_Start(stack_num)
        size = self.stack_size[stack_num - 1]
        return start + size - 1

    def Pop(self, stack_num):
        i = self.Find_Top_Index(stack_num)
        val = self.array[i]
        self.array[i] = None
        self.stack_size[stack_num - 1] -= 1
        return val

    def Push(self, stack_num, val):
        i = self.Find_Top_Index(stack_num)
        self.array[i + 1] = val
        self.stack_size[stack_num - 1] += 1

    def Peek(self, stack_num):
        i = self.Find_Top_Index(stack_num)
        return self.array[i]

    def Is_Empty(self, stack_num):
        start = find_start(stack_num)
        if array[start] == None:
            return True
        else:
            return False

    def Print(self):
        print(self.array)


# //----------------------------------------------------------------------------------//
# //
# //


def main():
    multistack = MultiStack(3)
    multistack.Print()
    multistack.Push(2, 5)
    multistack.Print()
    multistack.Push(2, 7)
    multistack.Print()
    print(multistack.Peek(2))


if __name__ == "__main__":
    main()
