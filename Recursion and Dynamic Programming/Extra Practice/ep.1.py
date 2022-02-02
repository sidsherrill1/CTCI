"""
Problem statement:
Write a program to calculate the sum of a list of numbers.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def Calc_Sum(l):
    if len(l) == (0):
        return 0

    if len(l) == 1:
        return l[0]

    return l[0] + Calc_Sum(l[1:])


# //***************************************************************************************//
# //
# //


def main():
    l = [1, 2, 3, 4, 5]
    print(Calc_Sum(l))


if __name__ == "__main__":
    main()
