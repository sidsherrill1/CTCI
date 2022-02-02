"""
Problem statement:
Permutations without Dups: Write a method to compute all permutations of a string of
unique characters.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def perm_rec(s, i, perms):
    if i == 0:
        perms.add(s[i])
        return perms

    perms = perm_rec(s, i - 1, perms)

    c = s[i]
    new_perms = set()
    for p in perms:
        # print(p)
        if len(p) > 1:
            for p_i in range(1, len(p)):
                left = p[:p_i]
                right = p[p_i:]
                new_perms.add(left + c + right)
                print(left + c + right)

        new_perms.add(c + p)
        new_perms.add(p + c)

    return new_perms


def perm(s):
    return perm_rec(s, len(s) - 1, set())


# //***************************************************************************************//
# //
# //


def main():
    print(perm("abc"))


if __name__ == "__main__":
    main()
