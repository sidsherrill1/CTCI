"""
Problem statement:
Print all permutations of a string.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def Perms_Helper(s, perms, c_i):
    c = s[c_i]
    if c_i == 0:
        return {c}

    perms = Perms_Helper(s, perms, c_i - 1)

    new_perms = set()
    for perm in perms:
        new_perms.add(c + perm)
        new_perms.add(perm + c)
        for i in range(1, len(perm)):
            new_perm = perm[:i] + c + perm[i:]
            new_perms.add(new_perm)

    return new_perms


def Perms(s):
    return Perms_Helper(s, set(), len(s) - 1)


# //***************************************************************************************//
# //
# //


def main():
    s = "abc"
    print(Perms(s))


if __name__ == "__main__":
    main()
