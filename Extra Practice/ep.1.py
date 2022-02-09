"""
Problem statement:
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target. You may assume that each input would have exactly one
solution, and you may not use the same element twice. You can return the answer in
any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

# //----------------------------------------------------------------------------------//
# //
# //


def two_sum(l, target):
    for i_a in range(len(l) - 1):
        a = l[i_a]
        for i_b in range(i_a + 1, len(l)):
            b = l[i_b]
            if a + b == target:
                return [i_a, i_b]
    return []


# //***************************************************************************************//
# //
# //


def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))

    nums = [3, 2, 4]
    target = 6
    print(two_sum(nums, target))

    nums = [3, 3]
    target = 6
    print(two_sum(nums, target))


if __name__ == "__main__":
    main()
