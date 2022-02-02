"""
Problem statement:
Write a function that takes two inputs n and m and outputs the number of unique paths
from the top left corner to the bottom right corner of an n x m grid.
Constraints: you can only move down or right 1 unit at a time.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def Get_Paths(r, c):
    if r == 1 or c == 1:
        print(f"r:{r}, c:{c}")
        return 1
    else:
        return Get_Paths(r - 1, c) + Get_Paths(r, c - 1)


# //***************************************************************************************//
# //
# //


def main():
    print(Get_Paths(2, 4))


if __name__ == "__main__":
    main()
