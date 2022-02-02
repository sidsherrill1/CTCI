"""
Problem statement:
Write a program to find the greatest common divisor of two integers.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def Find_GCD_rec_helper(a, b, gcd):
    if a % gcd == 0 and b % gcd == 0:
        return gcd

    return Find_GCD_rec_helper(a, b, gcd - 1)


def Find_GCD_rec(a, b):
    if b < a:
        temp = a
        a = b
        b = temp

    return Find_GCD_rec_helper(a, b, a)


def Find_GCD(a, b):
    if b < a:
        temp = a
        a = b
        b = temp

    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


# //***************************************************************************************//
# //
# //


def main():
    a = 40
    b = 48
    print(Find_GCD(a, b))
    print(Find_GCD_rec(a, b))


if __name__ == "__main__":
    main()
