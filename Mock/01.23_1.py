"""
Problem statement:

# implement a method to perform basic string compression using the counts of repeated characters.
# see test cases for examples.
# if the "compressed" string would not become smaller than the original string, your method shoudl 
# return the original string.
# you can assume the string has only uppsercase and lowercase letters (a-z)

EXAMPLE:
data =
[
    ('aabcccccaaa', 'a2b1c5a3'),
    ('abcdef', 'abcdef')
]


"""

# //----------------------------------------------------------------------------------//
# //
# //


def Comp_String(s):
    if len(s) == 0:
        return ""

    rv = []
    count = 1
    for i, c in enumerate(s):
        if i == 0:
            rv.append(c)
            continue

        if c == s[i - 1]:
            count += 1

        elif c != s[i - 1]:
            rv.append(f"{count}{c}")x
            count = 1

    rv.append(str(count))

    if len(rv) > len(s):
        return s

    return "".join(rv)


# //***************************************************************************************//
# //
# //


def main():
    s1 = "aabcccccaaa"
    print(Comp_String(s1))
    s2 = "abcdef"
    print(Comp_String(s2))


if __name__ == "__main__":
    main()
