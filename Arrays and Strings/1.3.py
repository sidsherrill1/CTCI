"""
Problem statement:
UFLify: Write a method rto replace all spaces in a string with '%20'. YOu may assume that the string has sufficient space at the end to hold the additional characters, and then you are given the "true" length of the string.

EXAMPLE
Input: "Mr John Smith     ",13
Output: "Mr%20John%20Smith"
"""

# //----------------------------------------------------------------------------------//
# //
# //


def URLIfy(s):
    s = s.strip()
    s_list = s.split(" ")
    while "" in s_list:
        s_list.remove("")
    return "%20".join(s_list)


# //***************************************************************************************//
# //
# //


def main():
    s = "Mr John    Smith     "
    print(URLIfy(s))


if __name__ == "__main__":
    main()
