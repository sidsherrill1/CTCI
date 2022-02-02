"""
Problem statement:
Write a function that counts the number of ways  you can partition n objects
using parts up to m.
source: https://www.youtube.com/watch?v=ngCos392W4w
"""

# //----------------------------------------------------------------------------------//
# //
# //


def part(n, m):
    if n == 0 or m == 1:
        return 1

    if m == 0 or n < 0:
        return 0

    return part(n - m, m) + part(n, m - 1)


# //***************************************************************************************//
# //
# //


def main():
    print(part(2, 2))


if __name__ == "__main__":
    main()
