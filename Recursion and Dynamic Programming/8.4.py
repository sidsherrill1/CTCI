"""
Problem statement:
Write a method to return all subsets of a set.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def Return_All_Subsets(s):
    subsets = [set()]
    for val in s:
        new_subsets = []
        for s in subsets:
            new_s = s.copy()
            new_s.add(val)
            new_subsets.append(new_s)
        subsets += new_subsets

    return subsets


# //***************************************************************************************//
# //
# //


def main():
    s = {"a", "b", "c"}
    print(Return_All_Subsets(s))


if __name__ == "__main__":
    main()
