"""
Problem statement:
Given two sorted arrays/lists, we want to merge them together, and imagine that A has
enough space in the end of it to accomodate B.

A = [10,14,17,None,None]
B = [2,9]
return [1,2,4,7,9]

A = [1,4,7,None,None]
B = [2,9]

A = [1,4,7,None,9]
B = [2,None]

A = [1,4,None,7,9], A_i = 1, B_i = 0, A_end = 2, 
B = [2,None]

A = [1,None,4,7,9], temp = 2, A_i = 0, B_i = -1, A_end = 1, 
B = [None,None]

"""

# //----------------------------------------------------------------------------------//
# //
# //


def merge(A, B, i_end):
    A_end = i_end + len(B)
    A_i = i_end
    B_i = len(B) - 1
    while B_i >= 0:

        print(f"A_i: {A_i}, B_i: {B_i}")

        if A[A_i] >= B[B_i] and A_i >= 0:
            temp = A[A_i]
            A[A_i] = None
            A_i -= 1
        else:
            temp = B[B_i]
            B[B_i] = None
            B_i -= 1

        A[A_end] = temp
        A_end -= 1

    return A


# //***************************************************************************************//
# //
# //


def main():
    A = [10, 14, 17, None, None]
    B = [2, 9]
    print(merge(A, B, 2))


if __name__ == "__main__":
    main()
