"""
Problem statement:
Parens: implement an algorithm to print all valid (i.e., properly opened and closed)
combinations of n pairs of parenthesis.
EXAMPLE
input: 3
output: ()()(),()(()),(())(),((())),((),()) 
"""

# //----------------------------------------------------------------------------------//
# //
# //


def parens_rec(n, combs):
    if n == 0:
        return combs

    if n == 1:
        combs.add("()")
        return combs

    combs = parens_rec(n - 1, combs)

    new_combs = set()
    for c_str in combs:

        # wrap entire lot in ()
        new_combs.add(f"({c_str})")

        # add a new () to the end of every comb
        new_combs.add(c_str + ",()")

        # for each element of every comb, wrap it in a new ()
        c_list = c_str.split(",")
        for i, c in enumerate(c_list):
            new_c_list = c_list.copy()
            new_c_list[i] = f"({c})"
            new_combs.add(",".join(new_c_list))

    return new_combs


def parens(n):
    combs = parens_rec(n, set())
    for c in combs:
        print(c)


# //***************************************************************************************//
# //
# //


def main():
    parens(4)


if __name__ == "__main__":
    main()
