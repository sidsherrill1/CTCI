"""
Problem statement:
Magic Index: A magic index in an array A[0...n-1] is defined to be an index such that
A[i] = i. Given a sorted array of distinct integers, write a method to find a magic
index, if one exists, in array A.

Follow up: what if the values are not distinct?
"""

import math

# //----------------------------------------------------------------------------------//
# //
# //

# Binary search (best for sorted list)
def Find_Magic_Index_Disctinct_Bin(A):
    """
    Binary search wrapper
    """
    return Find_Magic_Index_Disctinct_Bin_Rec(A, 0, len(A) - 1)


def Find_Magic_Index_Disctinct_Bin_Rec(A, start, end):
    """
    Binary search recursion
    """

    if end < start:
        return None

    mid = math.floor((end + start) / 2)
    if A[mid] == mid:
        return mid

    if A[mid] < mid:
        return Find_Magic_Index_Disctinct_Bin_Rec(A, mid + 1, end)
    elif A[mid - 1] < mid - 1:
        return Find_Magic_Index_Disctinct_Bin_Rec(A, start, mid - 1)
    else:
        return None


# //----------------------------------------------------------------------------------//
# //
# //


def Find_Magic_Index_Disctinct_Lin(A):
    """
    Linear search
    """
    for i in range(len(A)):
        if A[i] == i:
            return i

    return None


# //***************************************************************************************//
# //
# //


def main():
    A = [-5, -3, 0, 1, 4]
    print(Find_Magic_Index_Disctinct_Bin(A))


if __name__ == "__main__":
    main()
