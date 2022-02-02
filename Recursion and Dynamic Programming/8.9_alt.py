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


def add_paren(arr, left_rem, right_rem, string_arr, idx):
    if left_rem < 0 or right_rem < left_rem:  # invalid
        return
    if left_rem == 0 and right_rem == 0:  # out of left and right parentheses
        elem = "".join(string_arr)
        arr.append(elem)

    else:
        string_arr[idx] = "("  # add left and recurse
        add_paren(arr, left_rem - 1, right_rem, string_arr, idx + 1)

        string_arr[idx] = ")"  # add right and recurse
        add_paren(arr, left_rem, right_rem - 1, string_arr, idx + 1)


def generate_parens(n):
    results = []
    string_arr = ["*"] * n * 2
    add_paren(results, n, n, string_arr, 0)
    for e in results:
        print(e)


# //***************************************************************************************//
# //
# //


def main():
    generate_parens(3)


if __name__ == "__main__":
    main()
