"""
Problem statement:
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.
"""

# //----------------------------------------------------------------------------------//
# //
# //


def Ways_To_Climb(n):
    """
    Given the number of steps, returns the number of possible ways the child can run up the stairs.
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return Ways_To_Climb(n - 1) + Ways_To_Climb(n - 2) + Ways_To_Climb(n - 3)


# //----------------------------------------------------------------------------------//
# //
# //


def Ways_To_Climb_Init(n):
    return Ways_To_Climb_cached(n, [-1] * (n + 1))


def Ways_To_Climb_cached(i, memo):
    """
    Given the number of steps, returns the number of possible ways the child can run up the stairs.
    Caches results.
    """
    if i < 0:
        return 0
    elif i == 0:
        return 1

    if memo[i] == -1:
        memo[i] = Ways_To_Climb(i - 1) + Ways_To_Climb(i - 2) + Ways_To_Climb(i - 3)

    return memo[i]


# //***************************************************************************************//
# //
# //


def main():
    print(Ways_To_Climb(3))
    print(Ways_To_Climb(5))
    print(Ways_To_Climb_Init(3))
    print(Ways_To_Climb_Init(5))


if __name__ == "__main__":
    main()
