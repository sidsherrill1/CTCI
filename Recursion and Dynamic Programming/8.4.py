"""
Problem statement:
Write a method to return all subsets of a set.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def Return_All_Subsets(s):
    all_subsets = []
    return Return_All_Subsets_rec(s, all_subsets)


def Return_All_Subsets_rec(s, all_subsets):

    if len(s) == 0:
        return

    if s not in all_subsets:
        all_subsets.append(s)

    for val in s:
        new_s = s.copy()
        new_s.remove(val)
        Return_All_Subsets_rec(new_s, all_subsets)

    return all_subsets


# //***************************************************************************************//
# //
# //


def main():
    s = {"a", "b", "c"}
    print(Return_All_Subsets(s))


if __name__ == "__main__":
    main()
