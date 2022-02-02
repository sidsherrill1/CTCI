"""
Problem statement:
Write a program of recursion list sum.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def rec(l):
    if len(l) == 0:
        return 0

    if type(l[0]) == int:
        return l[0] + rec(l[1:])
    elif type(l[0]) == list:
        return l[0][0] + rec(l[0][1:]) + rec(l[1:])


# //***************************************************************************************//
# //
# //


def main():
    l = []
    l = [1]
    l = [[1]]
    l = [1, 2, [3, 4], [5, 6]]
    print(rec(l))


if __name__ == "__main__":
    main()
