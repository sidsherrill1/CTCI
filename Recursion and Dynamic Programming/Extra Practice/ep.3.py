"""
Problem statement:
Write a program to the get factorial of a non-negative integer.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def Get_Fact(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return n * (Get_Fact(n - 1))


# //***************************************************************************************//
# //
# //


def main():
    print(Get_Fact(4))


if __name__ == "__main__":
    main()
