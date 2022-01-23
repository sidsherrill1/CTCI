"""
Problem statement:
Write an algorithm to determine if a number is prime.
"""
import math

# //----------------------------------------------------------------------------------//
# //
# //


def Check_If_Prime(num):
    num_sqrt = int(math.sqrt(num))
    for i in range(2, num_sqrt + 1):
        if num % i == 0:
            return False
    return True


# //***************************************************************************************//
# //
# //


def main():
    print(Check_If_Prime(7))  # True
    print(Check_If_Prime(16))  # False
    print(Check_If_Prime(71))  # True
    print(Check_If_Prime(21))  # False
    print(Check_If_Prime(11))  # True


if __name__ == "__main__":
    main()
