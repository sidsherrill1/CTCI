"""
Problem statement:
Implement an algorith m to determine if a string has all unique characters.
What if you cannot use additoinal dat structures?
"""

# //----------------------------------------------------------------------------------//
# //
# //


def Is_Unique(s):
    characters = set()
    for c in s:
        if c in characters:
            return False
        else:
            characters.add(c)
    return True


# //----------------------------------------------------------------------------------//
# //
# //


def Is_Unique_No_Set(s):
    characters = ""
    for c in s:
        if c in characters:
            return False
        else:
            characters += c
    return True


# //***************************************************************************************//
# //
# //


def main():
    s = "abcdefg"
    print(Is_Unique(s))
    print(Is_Unique_No_Set(s))
    s = "abcddef"
    print(Is_Unique(s))
    print(Is_Unique_No_Set(s))


if __name__ == "__main__":
    main()
