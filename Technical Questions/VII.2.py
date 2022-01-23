"""
Problem statement:
Given a shorter string and a longer string, find all permutations of the 
shorter string within the longer string.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def build_dict_from_string(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


def Find_Perms(s, l):
    perms = []
    s_d = build_dict_from_string(s)
    for i in range(len(l) - len(s)):
        sub = l[i : i + len(s)]
        sub_d = build_dict_from_string(sub)
        if s_d == sub_d:
            perms.append(sub)
    return perms


# //***************************************************************************************//
# //
# //


def main():
    s = "abbc"
    l = "cbabadcbbabbcbabaabccbabc"
    print(Find_Perms(s, l))


if __name__ == "__main__":
    main()
