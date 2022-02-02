"""
Problem statement:
Towers of Hanoi: In the class problem of the Towers of Hanoi, you have 3 towers and N disks
of different sizes which can slide onto any tower. The puzzle starts with disks sorted
in ascending order of size from top to bottom (i.e. each disk sits on top of an even larger
one). You have the following constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using stacks.
"""

# //----------------------------------------------------------------------------------//
# //
# //


from imp import source_from_cache
from inspect import stack


class Stack:
    def __init__(self, disks):
        self.disks = disks
        self.size = len(disks)

    def pop(self):
        popped = self.disks.pop(self.size - 1)
        self.size -= 1
        return popped

    def push(self, disk):
        self.disks.append(disk)
        self.size += 1


def Towers_of_Hanoi_rec(n_disks, source, buffer, destination):
    if n_disks == 1:
        popped = source.pop()
        destination.push(popped)
        return source, buffer, destination

    Towers_of_Hanoi_rec(n_disks - 1, source, destination, buffer)
    popped = source.pop()
    destination.push(popped)
    Towers_of_Hanoi_rec(n_disks - 1, buffer, source, destination)

    return source, buffer, destination


def Towers_of_Hanoi(n_disks):
    disks = [x for x in range(n_disks, 0, -1)]

    source = Stack(disks)
    buffer = Stack([])
    destination = Stack([])

    return Towers_of_Hanoi_rec(n_disks, source, buffer, destination)


# //***************************************************************************************//
# //
# //


def main():
    n_disks = 3
    source, buffer, destination = Towers_of_Hanoi(n_disks)
    print(source.disks)
    print(buffer.disks)
    print(destination.disks)


if __name__ == "__main__":
    main()
