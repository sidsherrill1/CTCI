"""
Problem statement:
Implement and test and min and max heap.
"""

import math

# //----------------------------------------------------------------------------------//
# //
# //


def Min_Insert(heap, val):
    if len(heap) == 0:
        heap.append(val)
        return heap

    heap.append(val)

    # check if parent is less than val
    val_i = len(heap) - 1
    while val_i > 0:
        parent_i = math.floor((val_i - 1) / 2)  # [1,2,3,2.l,2.r,3.l,3.r]
        parent = heap[parent_i]
        if parent > val:
            heap[parent_i] = val
            heap[val_i] = parent
            val_i = parent_i
        else:
            break

    return heap


def Min_Extract(heap):
    # swap the first val with the last
    top = heap[0]
    bottom = heap[len(heap) - 1]
    heap[0] = bottom
    heap[len(heap) - 1] = top

    # pop off the last
    heap.pop(len(heap) - 1)

    # bubble down the new first val
    i = 0
    new_top = heap[i]
    while True:
        if i == len(heap) - 1:
            break

        left_child_i = (i * 2) + 1
        left_child = heap[left_child_i]
        right_child_i = (1 * 2) + 2
        # If there's only a left child, compare new_top with left
        if right_child_i > len(heap) - 1:
            if new_top < left_child:
                break
            else:
                heap[i] = left_child
                heap[left_child_i] = new_top
                break

        # If there is both a left and right child, swap with the smaller one
        elif right_child_i <= len(heap) - 1:
            right_child = heap[right_child_i]
            if new_top < left_child and new_top < right_child:
                break

            if left_child < right_child:
                heap[i] = left_child
                heap[left_child_i] = new_top
                i = left_child_i

            elif right_child < left_child:
                heap[i] = right_child
                heap[right_child_i] = new_top
                i = right_child_i

    return heap


# //***************************************************************************************//
# //
# //


def main():
    heap = []
    heap = Min_Insert(heap, 3)
    print(heap)
    heap = Min_Insert(heap, 9)
    print(heap)
    heap = Min_Insert(heap, 5)
    print(heap)
    heap = Min_Insert(heap, 1)
    print(heap)
    heap = Min_Insert(heap, 8)
    print(heap)

    # //---------------------//
    heap = Min_Extract(heap)
    print(heap)
    heap = Min_Extract(heap)
    print(heap)
    heap = Min_Extract(heap)
    print(heap)
    heap = Min_Extract(heap)
    print(heap)


if __name__ == "__main__":
    main()
