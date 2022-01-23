"""
Problem statement:
Implement Get Bit, Set Bit, Clear Bit and Upate Bit.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def Get(num, i):
    mask = 1 << i
    test = num & mask
    if test == 0:
        return 0
    else:
        return 1


def Set(num, i):
    mask = 1 << i
    return mask ^ num


def Clear(num, i):
    mask = ~(1 << i)
    return mask & num


def Update(num, i, binary_value):
    val = int(binary_value)
    mask = ~(val << i)
    return mask & num


# //***************************************************************************************//
# //
# //


def main():
    num = 8
    print(bin(Get(num, 3)))
    print(bin(Set(num, 0)))
    print(bin(Clear(num, 0)))


if __name__ == "__main__":
    main()
