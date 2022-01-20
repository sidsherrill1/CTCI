"""
Problem statement:
Given two strings, write a method to decide if one is a permutation of the other.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def Build_Dict(s, d):
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1


def Check_Permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    d1 = {}
    d2 = {}
    Build_Dict(s1, d1)
    Build_Dict(s2, d2)
    if d1 == d2:
        return True
    else:
        return False


# //***************************************************************************************//
# //
# //


def main():
    s1 = "abcd"
    s2 = "dcba"
    print(Check_Permutation(s1, s2))


if __name__ == "__main__":
    main()
