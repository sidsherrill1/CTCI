"""
Problem statement:
Recursive Multiply: Write a recursive function to multiply two positive integers
without using the * operator. You can use addition, subtraction, and bit shifting,
but you should minimize the number of those operations.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def Rec_Mult(a, b):
    if b == 0:
        return 0
    else:
        return a + Rec_Mult(a, b - 1)


# //***************************************************************************************//
# //
# //


def main():
    print(Rec_Mult(10, 10))


if __name__ == "__main__":
    main()
