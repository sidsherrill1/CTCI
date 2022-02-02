"""
Problem statement:
Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements into any
other data structure (such as an array). The stack supports the following operations:
push, pop, peek, and isEmpty.
"""

import stack
from sys import maxsize

# //----------------------------------------------------------------------------------//
# //
# //

def sort_stack(s):
    
    temp_s = stack.Stack()
    while s.head != None:

        temp = s.pop()

        if temp_s.isEmpty() or temp < temp_s.peek():
            temp_s.push(temp)

        else:
            while not temp_s.isEmpty() and temp_s.peek() < temp:
                s.push(temp_s.pop())
            temp_s.push(temp)
                
    return temp_s

# //----------------------------------------------------------------------------------//
# //
# //


def main():
    s = stack.Stack()
    s.push(25)
    s.push(15)
    s.push(35)
    s.push(20)
    sorted_s = sort_stack(s)
    sorted_s.print()



if __name__ == "__main__":
    main()
